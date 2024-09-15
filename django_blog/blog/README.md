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



# Blog Post Management

## CRUD Operations

### List Posts
- **URL:** `/posts/`
- **Description:** Displays a list of all blog posts.

### View Post Details
- **URL:** `/posts/<id>/`
- **Description:** Shows details of a specific blog post.

### Create Post
- **URL:** `/posts/new/`
- **Description:** Allows authenticated users to create a new blog post.

### Edit Post
- **URL:** `/posts/<id>/edit/`
- **Description:** Allows authors to edit their posts.

### Delete Post
- **URL:** `/posts/<id>/delete/`
- **Description:** Allows authors to delete their posts.

## Testing

- Test CRUD operations with valid and invalid data.
- Ensure proper access control and permissions are enforced.

## Permissions

- **Create:** Only authenticated users can create posts.
- **Edit/Delete:** Only the author of a post can edit or delete it.


## Comment System

### Overview
The comment system allows users to engage with blog posts by adding, editing, and deleting comments. This feature fosters community interaction and discussion on individual blog posts.

### Features
1. **Add Comments**: Authenticated users can add comments to any blog post.
2. **Edit Comments**: Comment authors can edit their comments.
3. **Delete Comments**: Comment authors can delete their comments.
4. **View Comments**: All users can view comments associated with a blog post.

### Usage
**Adding a Comment**
- Navigate to the Blog Post
- Click "Add Comment"
- Fill in the Comment Form
- Submit

**Editing a Comment**
- Locate Your Comment
- Click "Edit"
- Update Your Comment
- Save Changes

**Deleting a Comment**
- Find Your Comment
- Click "Delete"
- Confirm Deletion

### Permissions
- **Adding Comments**: Any authenticated user can add comments.
- **Editing Comments**: Only the author of a comment can edit it.
- **Deleting Comments**: Only the author of a comment can delete it.

### URL Patterns
- **Add Comment**: `/posts/<int:post_id>/comments/new/`
- **Edit Comment**: `/comments/<int:comment_id>/edit/`
- **Delete Comment**: `/comments/<int:comment_id>/delete/`

### Error Handling
- **Unauthorized Actions**: Users attempting to edit or delete comments they did not author will be redirected to the blog post page.
- **Form Validation**: Invalid form submissions will show appropriate error messages.

### Example
Here’s an example of the URL structure for managing comments:
- **Add Comment**: `/posts/1/comments/new/` (for post ID 1)
- **Edit Comment**: `/comments/5/edit/` (for comment ID 5)
- **Delete Comment**: `/comments/5/delete/` (for comment ID 5)

### Notes
- Ensure you are logged in to add, edit, or delete comments.
- Comments are displayed in chronological order with the newest comments at the end of the list.


## Tagging and Search Functionality

### Tagging Posts
- **Add Tags**: When creating or editing a post, use the checkbox list to select or add tags.
- **View Tags**: Tags are displayed on the post detail page and link to pages showing all posts with that tag.

### Searching Posts
- **Search Bar**: Located on the blog's main page and in the header of all pages.
- **Search Function**: Enter keywords to find posts by title, content, or tags.
- **Search Results**: Results are displayed on a dedicated search results page.

### URL Patterns
- **Tags**: `/tags/<tag_name>/` - Shows posts associated with a specific tag.
- **Search**: `/search/` - Shows posts matching the search query.
