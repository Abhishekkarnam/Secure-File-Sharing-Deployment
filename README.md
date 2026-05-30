# Secure File Sharing

## Docker + Neon PostgreSQL Deployment

### 1. Create the Neon database
1. Create a PostgreSQL database in Neon.
2. Copy the connection string from Neon.
3. In Render or your Docker host, set `DATABASE_URL` to that Neon string.
4. If Neon gives you a URL that starts with `postgres://`, the backend already normalizes it to `postgresql+psycopg2://`.

### 2. Build the backend Docker image
From the repository root:

```bash
docker build -t secure-file-sharing-backend .
```

### 3. Run the container locally
Pass the Neon connection string and JWT secret as environment variables:

```bash
docker run --rm -p 10000:10000 ^
	-e DATABASE_URL="your-neon-postgres-url" ^
	-e JWT_SECRET_KEY="your-secret-key" ^
	secure-file-sharing-backend
```

On PowerShell, use backticks instead of `^`.

### 4. Deploy on Render
1. Create a new Web Service from the repository.
2. Choose the Docker deployment option.
3. Render will build from the root `Dockerfile`.
4. Add these environment variables:
	 - `DATABASE_URL`
	 - `JWT_SECRET_KEY`
5. Leave `PORT` to Render. The container already binds to it.

### 5. Deploy the frontend on Vercel
1. Deploy the frontend as a static site from this repo.
2. Keep the Vercel rewrites in [vercel.json](vercel.json) so the HTML pages and static assets load correctly.

### 6. Local frontend testing
If you are testing locally with Flask, open the app at `http://127.0.0.1:5000/`.
