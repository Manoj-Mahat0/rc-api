import requests
import time

# IP Webcam snapshot URL
ipcam_url = "http://192.168.166.149:8080/shot.jpg"
image_path = "/home/pi/frame.jpg"

# Upload URL
upload_url = "https://videostream-latlong.onrender.com/upload-frame/"

while True:
    try:
        # Capture frame from mobile camera
        response = requests.get(ipcam_url, timeout=5)
        with open(image_path, "wb") as f:
            f.write(response.content)
        print("✅ Frame captured")

        # Upload to FastAPI server
        with open(image_path, "rb") as f:
            files = {'file': f}
            res = requests.post(upload_url, files=files)

        print("📤 Sent. Status:", res.status_code, "| Body:", res.text)

    except Exception as e:
        print("❌ Error:", e)

    # Wait 10 seconds before next upload
    time.sleep(10)
