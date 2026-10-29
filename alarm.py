print(f"Alarm set for {alarm_time}")
    print("Waiting for alarm...")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("⏰ WAKE UP! ALARM RINGING!")

            # Play alarm sound 10 times
            for _ in range(10):
                winsound.Beep(1000, 800)
                time.sleep(0.2)

            break

        time.sleep(1)

if __name__ == "__main__":
    set_alarm()
