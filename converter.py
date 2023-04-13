from main import media_processor


if __name__ == '__main__':
    processor = media_processor()
    processor.to_mp4_converter()
    #i = input("would you like to specify a dir (defaults to whacontent in ftpuser's home): ")
    #if i:
    #    processor.to_mp4_converter(i)
    #else:
    #    processor.to_mp4_converter()