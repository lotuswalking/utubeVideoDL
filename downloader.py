from apscheduler.schedulers.background import BackgroundScheduler


def delete_first_line():
    with open('data.txt', 'r+') as f:
        lines = f.readlines()

        if lines:
            first_line = lines[0]
            lines = lines[1:]

            f.seek(0)
            f.writelines(lines)

            f.truncate()

    # Do something with the first line
    print(first_line.strip())


scheduler = BackgroundScheduler()
scheduler.add_job(delete_first_line, 'interval', minutes=1)
scheduler.start()
