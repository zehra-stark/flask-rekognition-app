# 🚀 Flask AWS Rekognition App with EC2 Backup & Secure Access

## 📌 Project Overview

This project is a complete web-based image recognition system built with **Flask** and **AWS Rekognition**. Users can upload images, and the app detects objects, scenes, or concepts in them using Amazon Rekognition.

Additionally, the project emphasizes **best practices in AWS** by demonstrating how to:
- Backup the EC2 instance using **Amazon Machine Images (AMIs)** and **Snapshots**
- Set up **secure access** using **SSH key pairs**

This makes the project a **mini full-stack + DevOps deployment** suitable for academic, personal, and cloud portfolio purposes.

---

## ✨ Features

- 📷 Upload images via a sleek web interface
- 🧠 Detect labels using Amazon Rekognition (AI/ML powered)
- 🔒 Secure EC2 access via SSH key pairs
- 💾 Backup EC2 instance using AMIs and Snapshots
- 🖼️ Display labeled results along with the uploaded image
- 🌐 Host Flask app on AWS EC2 instance

---

## ⚙️ Tools & Technologies Used

| Tool | Why It Was Used |
|------|------------------|
| **Flask** | Lightweight Python web framework for building the web app |
| **Amazon Rekognition** | AI service to detect labels in images |
| **Amazon EC2** | Host and run the Flask application on a virtual server |
| **AWS AMI** | For full instance backup, enabling re-deployment anytime |
| **AWS Snapshot** | Backup of EBS volumes (data disks) |
| **SSH Key Pair** | Secure, passwordless login to EC2 |
| **Git & GitHub** | Version control and code collaboration |

---

## 🛠️ How to Set Up the Project

1. **Launch an EC2 instance**
   - Choose Amazon Linux 2 AMI
   - Select t2.micro (Free Tier)
   - Add your key pair for secure access
   - Open ports `22` (SSH) and `5000` (Flask) in the **Security Group**

2. **SSH into your EC2 instance**
```bash
ssh -i "your-key.pem" ec2-user@your-ec2-public-dns

3. **Install system dependencies**
```bash
sudo yum update -y
sudo yum install git python3 -y

4. **Clone your GitHub repo**
```bash
git clone https://github.com/yourusername/flask-rekognition-app.git
cd flask-rekognition-app

5. **Install Python dependencies**
```bash
pip3 install flask boto3

⚙️ How to Run the Flask App
```bash
python3 app.py

Then open your browser and visit:
http://<EC2-Public-IP>:5000

🔐 How I Secured EC2 Access
---------------------------
- Used SSH Key Pair while launching EC2  
- Disabled password-based login  
- Security group allowed only:  
  - SSH (Port 22)  
  - Flask (Port 5000)  

💾 How I Backed Up EC2
-----------------------
✅ Create an AMI  
- Go to EC2 → Instances  
- Select instance → Actions → Image and Templates → Create Image  
- This includes OS, config, and volume  

✅ Create a Snapshot  
- Go to EC2 → Elastic Block Store → Volumes  
- Select volume → Actions → Create Snapshot  
- Good for backing up just the data (volume only)  

📚 What I Learned
------------------
- How Flask integrates with AWS Rekognition  
- Managing cloud infrastructure using EC2  
- Securely connecting to instances via SSH keys  
- Creating full and partial backups using AMIs & Snapshots  
- Hosting and deploying a Python web app on the cloud  

📂 Dependencies
----------------
- Flask  
- Boto3  
- AWS CLI *(optional for manual snapshot/image creation)*  

**Install them with:**

```bash
pip3 install flask boto3

🚀 How This Project Works
--------------------------
- User uploads an image  
- Flask saves the image temporarily  
- App sends the image to AWS Rekognition  
- Boto3 receives labels from Rekognition  
- Labels and the image are displayed in the browser  

🧪 Real-Time Example
---------------------
**Uploaded image**: Bugatti  

**Detected labels:**
- Car  
- Sports Car  
- Vehicle  
- Alloy Wheel  
- Tire  

🧑‍💻 Author
------------
🔗 GitHub: [zehra-stark](https://github.com/zehra-stark)

🏁 To Run This Project Yourself
-------------------------------
```bash
git clone https://github.com/zehra-stark/flask-rekognition-app.git
cd flask-rekognition-app
pip3 install -r requirements.txt  # or manually install
python3 app.py

