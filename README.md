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

## Setup

1. Clone the repo:

```bash
git clone https://github.com/<your-username>/e-library-backend.git
cd e-library-backend
