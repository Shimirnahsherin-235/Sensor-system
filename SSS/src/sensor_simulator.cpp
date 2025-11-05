#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <thread>
#include <chrono>

using namespace std;

float getTemperature() {
    return 20 + rand() % 20; // 20–40°C
}

float getHumidity() {
    return 40 + rand() % 40; // 40–80%
}

float getGasLevel() {
    return 100 + rand() % 400; // 100–500 ppm
}

int main() {
    srand(time(0));

    ofstream file("sensor_data.csv");
    if (!file.is_open()) {
        cout << "❌ Error: Unable to open file!" << endl;
        return 1;
    }

    // Write CSV header
    file << "Timestamp,Temperature,Humidity,GasLevel\n";
    file.close();

    cout << "✅ Sensor Simulator Started. Writing to sensor_data.csv\n";

    while (true) {
        float temp = getTemperature();
        float hum = getHumidity();
        float gas = getGasLevel();

        // Get current time
        time_t now = time(0);
        string timestamp = ctime(&now);
        timestamp.pop_back(); // remove newline

        ofstream file("sensor_data.csv", ios::app);
        file << timestamp << "," << temp << "," << hum << "," << gas << "\n";
        file.close();

        cout << "🌡️ Temp: " << temp << "°C, 💧 Hum: " << hum << "%, 🧪 Gas: " << gas << " ppm" << endl;

        this_thread::sleep_for(chrono::seconds(3)); // update every 3 seconds
    }

    return 0;
}
