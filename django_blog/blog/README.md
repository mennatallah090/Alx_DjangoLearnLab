# Django Blog Authentication System

## Registration

- **Access Registration Page:**
  Navigate to `/register` in your web browser to access the registration page.

- **Registration Form:**
  - **Username:** Enter a unique username.
  - **Email:** Provide a valid email address.
  - **Password:** Choose a strong password and confirm it.

- **Submission:**
  Click the “Register” button to submit the form.
  Upon successful registration, you will be redirected to the login page with a confirmation message.

## Login

- **Access Login Page:**
  Navigate to `/login` to access the login page.

- **Login Form:**
  - **Username:** Enter your registered username.
  - **Password:** Enter the corresponding password.

- **Submission:**
  Click the “Login” button to authenticate.
  On successful login, you will be redirected to your profile page.

## Logout

- **Access Logout:**
  Navigate to `/logout` to log out of your session.

- **Effect:**
  You will be logged out and redirected to the login page.

## Profile Management

- **Access Profile Page:**
  Navigate to `/profile` to view and edit your profile details.

- **Profile Form:**
  - **Email:** You can update your email address.
  - **Bio:** Enter or update your profile bio.
  - **Profile Picture:** Upload or update your profile picture.

- **Submission:**
  Click the “Update Profile” button to save changes.
  Upon successful update, you will receive a confirmation message and see the updated profile information.

## Testing Instructions

1. **Run the Development Server:**
   ```bash
   python manage.py runserver
