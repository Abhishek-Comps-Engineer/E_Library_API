# E-Library Backend

This is a **FastAPI backend** for an E-Library system. It supports **JWT authentication**, **role-based access**, and **book upload management**. Authors can upload books (PDF + cover), and admins can approve or reject them. Readers can browse and download approved books.

## Features

- User registration & login with JWT
- Role-based dashboards: Reader, Author, Admin
- Author book upload (PDF + cover image)
- Admin review & approval of books
- Secure file download for approved books
- PostgreSQL database integration
- FastAPI endpoints with Pydantic schemas
- Environment-based configuration

## Architecture 
<img width="1536" height="1024" alt="Architecture_E_Library_backend" src="https://github.com/user-attachments/assets/0c03dd41-c621-4d8d-9f68-2bb238479c86" />

## Setup

1. Clone the repo:

```bash
git clone https://github.com/abhisheksharma-swe/e-library-backend.git
cd e-library-backend
