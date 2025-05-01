from ultralytics import YOLO
model = YOLO("best.pt")
success = model.export(format="onnx", simplify=True)  # export the model to onnx format
assert success
print("转换成功")
