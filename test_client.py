import tritonclient.grpc as grpcclient
import numpy as np
import time

TRITON_URL = "localhost:8001"
MODEL_NAME = "tiny_llama"

client = grpcclient.InferenceServerClient(url=TRITON_URL, verbose=False)

prompt = "Explain artificial intelligence in one line."
inputs = grpcclient.InferInput("text_input", [1], "BYTES")
inputs.set_data_from_numpy(np.array([prompt.encode("utf-8")], dtype=object))

def stream_callback(result, error):
    if error:
        print("❌ Stream error:", error)
    else:
        try:
            text = result.as_numpy("text_output")[0].decode("utf-8")
            print("🧠 Partial Output:", text)
        except Exception:
            pass

client.start_stream(callback=stream_callback)
client.async_stream_infer(model_name=MODEL_NAME, inputs=[inputs])

time.sleep(10)
client.stop_stream()
print("\n✅ Streaming inference complete!")
