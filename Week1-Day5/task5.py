def step(altitude, velocity, fuel, thrust):
    new_velocity = velocity + 1.62 - thrust * 0.5
    new_altitude = altitude - new_velocity
    new_fuel = fuel - thrust
    return new_altitude, new_velocity, new_fuel


def autopilot(altitude, velocity, fuel):
    # نخفض سرعة النزول المطلوبة عند الاقتراب من السطح،
    # ونحسب الدفع اللازم للوصول إليها مع مراعاة الوقود.
    target_speed = min(
        30, max(2, (4 * max(altitude - 5, 0)) ** 0.5)
    )
    thrust = 2 * (velocity + 1.62 - target_speed)
    return min(10, fuel, max(0, thrust))


def play(automatic=False):
    altitude = 1000
    velocity = 0
    fuel = 200
    seconds = 0

    while altitude > 0:
        print(
            f"t={seconds}s | altitude: {altitude:.1f} m | "
            f"speed: {velocity:.1f} m/s | fuel: {fuel:.2f}"
        )

        if automatic:
            thrust = autopilot(altitude, velocity, fuel)
            print(f"Auto thrust: {thrust:.2f}")
        else:
            try:
                thrust = float(input("Thrust (0-10): "))
            except ValueError:
                print("Enter a number.")
                continue

            if not (0 <= thrust <= 10):
                print("Choose a value from 0 to 10.")
                continue

            if thrust > fuel:
                print("Not enough fuel.")
                continue

        altitude, velocity, fuel = step(
            altitude, velocity, fuel, thrust
        )
        seconds += 1

    print("Safe landing" if velocity <= 3 else "Crashed")
    print(f"Final speed: {velocity:.2f} m/s")
    print(f"Fuel left: {fuel:.2f}")
    print(f"Flight time: {seconds} s")


if __name__ == "__main__":
    mode = input("Choose mode: 1 = manual, 2 = autopilot: ")
    play(automatic=(mode == "2"))
