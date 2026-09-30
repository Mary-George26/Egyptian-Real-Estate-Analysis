import kagglehub

# Download latest version
path = kagglehub.dataset_download("hassankhaled21/egyptian-real-estate-listings")

print("Path to dataset files:", path)

print("Download completed successfully!")