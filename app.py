import base64
import io
import torch
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, render_template, request, jsonify
from train import Net  # Import the Net class from your train.py file

app = Flask(__name__)
device = torch.device('cpu')

model = Net()
model.load_state_dict(torch.load("/mnt/pc3427_model.pth"))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.form:
        return jsonify({'error': 'No image data found'}), 400

    image_data = request.form['image'].split(',')[1]
    image_data = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_data)).convert('L')
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        prediction = output.argmax(dim=1).item()

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)