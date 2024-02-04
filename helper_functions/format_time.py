def format_processing_time(elapsed_time):
    minutes, seconds = divmod(elapsed_time, 60)
    seconds, milliseconds = divmod(seconds, 1)
    return f"{int(minutes):02}m:{int(seconds):02}s:{int(milliseconds * 1000)}ms"
