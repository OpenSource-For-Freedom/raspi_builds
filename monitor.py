# inital raspi pid mapping and monitoring framework 

from gpiozero 
import InputDevice, OutputDevice
import matplotlib.pyplot as plt
import time
# pid monitor status and input sequences (general) 
# define loop monitor pid
# define KEIO and KOIO based on inout pin

class PIDMonitor: #varying pid monitor hardware TBD
    def __init__(self, input_pin, output_pin):
        self.input_device = InputDevice(input_pin)
        self.output_device = OutputDevice(output_pin)
        self.data = {'time': [], 'input': [], 'output': []}

    def monitor_loop(self, duration_sec): # def KOIO and KOEO to not drain battery 
        start_time = time.time()

        while time.time() - start_time < duration_sec:
            current_time = time.time() - start_time
            input_value = self.input_device.value
            output_value = self.output_device.value

            self.data['time'].append(current_time)
            self.data['input'].append(input_value)
            self.data['output'].append(output_value)

            time.sleep(0.1)  # Adjust the sleep time as needed
# matplotlib (my fave :)- <)Visualization and mapping output if using raspi lcd screen only
    def plot_data(self):
        plt.plot(self.data['time'], self.data['input'], label='Input')
        plt.plot(self.data['time'], self.data['output'], label='Output')
        plt.xlabel('Time (s)')
        plt.ylabel('Value')
        plt.legend()
        plt.show()
# build function for CI/CD Mapping for KOIO status monitor
if __name__ == "__main__":
    pid_monitor = PIDMonitor(input_pin=17, output_pin=18)
    pid_monitor.monitor_loop(duration_sec=60)  # Monitor for 60 seconds
    pid_monitor.plot_data()