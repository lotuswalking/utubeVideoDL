from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import argparse

def main():
	parser = argparse.ArgumentParser(description="YouTube下载器，支持简单和全参数模式")
	parser.add_argument("url", help="YouTube视频URL")
	parser.add_argument("--audio-only", "-a", type=str, default="true", help="仅下载音频，true/false，默认true")
	parser.add_argument("--proxy", "-p", type=str, default="http://10.62.220.124:8899", help="代理地址，默认http://10.62.220.124:8899")
	args = parser.parse_args()

	url = args.url
	audio_only = args.audio_only.lower() == "true"
	proxy_addr = args.proxy
	proxies = {
		'http': proxy_addr,
		'https': proxy_addr,
	}
	yt = YouTube(url, proxies=proxies)
	print(f"视频标题: {yt.title}")
	# 文件名处理：保留字母、数字、下划线和中文
	safe_title = re.sub(r'[^A-Za-z0-9_\u4e00-\u9fff]', '', yt.title.replace(' ', ''))
	if audio_only:
		stream = yt.streams.filter(only_audio=True).first()
		print("下载音频...")
		ext = ".m4a" if stream and stream.mime_type and "m4a" in stream.mime_type else ".mp3"
	else:
		stream = yt.streams.get_highest_resolution()
		print("下载视频...")
		ext = ".mp4"
	filename = safe_title + ext
	stream.download(filename=filename)

if __name__ == "__main__":
	main()