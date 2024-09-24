# Social Media API

## Overview
This is a Social Media API built using Django and Django REST Framework. The API allows users to create, view, update, and delete posts and comments, providing a platform for social interaction.

## Table of Contents
- [Installation](#installation)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Posts Endpoints](#posts-endpoints)
  - [Comments Endpoints](#comments-endpoints)
- [Pagination and Filtering](#pagination-and-filtering)
- [Testing](#testing)

## Installation
...

## Authentication
...

## API Endpoints

### Posts Endpoints

#### 1. Create Post
- **Method**: `POST`
- **URL**: `/posts/`
- **Authentication**: Required (Token in headers)
- **Request Body**:
    ```json
    {
        "title": "My First Post",
        "content": "This is the content of my first post."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "author": "testuser",
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    }
    ```

#### 2. List Posts
- **Method**: `GET`
- **URL**: `/posts/`
- **Authentication**: Required (Token in headers)
- **Response**:
    ```json
    [
        {
            "id": 1,
            "author": "testuser",
            "title": "My First Post",
            "content": "This is the content of my first post.",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        ...
    ]
    ```

#### 3. Update Post
- **Method**: `PUT`
- **URL**: `/posts/{post_id}/`
- **Authentication**: Required (Token in headers)
- **Request Body**:
    ```json
    {
        "title": "Updated Title",
        "content": "Updated content."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "author": "testuser",
        "title": "Updated Title",
        "content": "Updated content.",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }
    ```

#### 4. Delete Post
- **Method**: `DELETE`
- **URL**: `/posts/{post_id}/`
- **Authentication**: Required (Token in headers)
- **Response**: `204 No Content`

### Comments Endpoints

#### 1. Create Comment
- **Method**: `POST`
- **URL**: `/comments/`
- **Authentication**: Required (Token in headers)
- **Request Body**:
    ```json
    {
        "post": 1,
        "content": "This is a comment."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "post": 1,
        "author": "testuser",
        "content": "This is a comment.",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    }
    ```

#### 2. List Comments
- **Method**: `GET`
- **URL**: `/comments/`
- **Authentication**: Required (Token in headers)
- **Response**:
    ```json
    [
        {
            "id": 1,
            "post": 1,
            "author": "testuser",
            "content": "This is a comment.",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        ...
    ]
    ```

#### 3. Update Comment
- **Method**: `PUT`
- **URL**: `/comments/{comment_id}/`
- **Authentication**: Required (Token in headers)
- **Request Body**:
    ```json
    {
        "content": "This is an updated comment."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "post": 1,
        "author": "testuser",
        "content": "This is an updated comment.",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }
    ```

#### 4. Delete Comment
- **Method**: `DELETE`
- **URL**: `/comments/{comment_id}/`
- **Authentication**: Required (Token in headers)
- **Response**: `204 No Content`

## Pagination and Filtering
- Use query parameters for pagination and filtering on the list endpoints:
  - **Pagination**: Use `?page=2` to get the second page of results.
  - **Filtering**: For posts, use `?search=keyword` to filter by title or content.

## Testing
You can test the API using tools like Postman or by running automated tests included in the project.
