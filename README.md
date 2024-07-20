# Two-Factor Authentication (2FA) Sample Web Application

## Overview

This project is a sample web application demonstrating the implementation of Two-Factor Authentication (2FA) using Flask, PyOTP, and QR codes. The purpose of this project is to understand the importance and benefits of 2FA, implement it on a sample web application, and test its effectiveness in enhancing security.

## Objectives

1. **Learn the Importance and Benefits of Two-Factor Authentication**:
   - Understand how 2FA adds an extra layer of security by requiring not only a password and username but also something that only the user has on them, i.e., a piece of information only they should know or have immediately to hand.

2. **Implement 2FA on a Sample Web Application**:
   - Develop a simple web application using Flask.
   - Generate and display a QR code for users to scan with their authenticator app.
   - Verify the OTP (One-Time Password) entered by the user.

3. **Test the 2FA Implementation and Ensure it Enhances Security**:
   - Ensuring that the implementation correctly verifies the OTP.
   - Confirm that the extra layer of authentication improves the security of the application.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **PyOTP**: A Python library for generating and verifying one-time passwords.
- **qrcode**: A Python library for generating QR codes.
- **base64**: A Python module for encoding and decoding base64 strings.
- **Bootstrap**: A front-end framework for designing responsive web pages.