from urllib.parse import urlparse

def nameFromUrl(url: str):
	return urlparse(url).path.rpartition("/")[-1].partition("-")[0]
