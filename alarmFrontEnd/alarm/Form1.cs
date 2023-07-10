using System;
using System.Windows.Forms;
using System.Net;
using System.IO;
using Newtonsoft.Json;
using MySql.Data.MySqlClient;

namespace AlarmInterface
{
    public partial class MainForm : Form
    {
        private bool alarmOn = false;
        private string currentDigit = "off";
        private WebClient webClient = new WebClient();
        private MySqlConnection connection = new MySqlConnection("server=localhost;user=root;database=alarm;port=3306;password=");
        private System.Windows.Forms.Timer timer;


        public MainForm()
        {
            InitializeComponent();
            UpdateUI();
            label4.Text = "Alarm ON";
            label1.Text = "Zone 1 is ON ";
            label2.Text = "Zone 2 is ON ";
            label3.Text = "Zone 3 is ON ";

            timer = new System.Windows.Forms.Timer();
            timer.Interval = 1000; // Polling interval in milliseconds (e.g., 5000ms = 5s)
            timer.Tick += Timer_Tick;
            timer.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            UpdateUI();
        }

        private void SetDigit(string digit)
        {
            currentDigit = digit;
            UpdateUI();
            if (alarmOn)
            {
                SendData();
            }
        }

        private void ToggleAlarm()
        {
            alarmOn = !alarmOn;
            UpdateUI();
            if (alarmOn)
            {
                SendData();
            }
        }

        private void SendData()
        {
            var data = new { current_digit = currentDigit, alarm_state = alarmOn ? "on" : "off" };
            var json = JsonConvert.SerializeObject(data);
            var response = webClient.UploadString("http://192.168.1.109:3000/api/data", json);
            Console.WriteLine(response);
        }

        private void UpdateUI()
        {
            label1.Text = currentDigit;

            try
            {
                var response = webClient.DownloadString("http://192.168.1.109:3000/api/data");
                dynamic data = JsonConvert.DeserializeObject(response);

                if (data.alarm_state == "on")
                {
                    label4.Text = "Alarm ON";
                    label1.Text = "Zone 1 is OFF ";
                    label2.Text = "Zone 2 is OFF ";
                    label3.Text = "Zone 3 is OFF ";
                    label1.BackColor = System.Drawing.Color.Green;
                    label2.BackColor = System.Drawing.Color.Green;
                    label3.BackColor = System.Drawing.Color.Green;
                    label4.BackColor = System.Drawing.Color.Red;

                    if (data.current_digit == 1)
                    {
                        label1.Text = "Zone 1 is On";
                        label1.BackColor = System.Drawing.Color.Red;

                    }
                    else if (data.current_digit == 2)
                    {
                        label2.Text = "Zone 2 is On";
                        label2.BackColor = System.Drawing.Color.Red;
                    }
                    else if (data.current_digit == 3)
                    {
                        label3.Text = "Zone 3 is On";
                        label3.BackColor = System.Drawing.Color.Red;
                    }

                }

                else
                {
                    label4.Text = "Alarm OFF";
                    label1.Text = "Zone 1 is OFF ";
                    label2.Text = "Zone 2 is OFF ";
                    label3.Text = "Zone 3 is OFF ";
                    label1.BackColor = System.Drawing.Color.Green;
                    label2.BackColor = System.Drawing.Color.Green;
                    label3.BackColor = System.Drawing.Color.Green;
                    label4.BackColor = System.Drawing.Color.Green;
                }
            }
            catch (Exception ex)
            {


                Console.WriteLine(ex.Message);
            }
        }

        public class ApiResponse
        {
            public string Message { get; set; }
        }


        private void SendButtonCommand(string _button)
        {
            var data = new { button = _button };
            var json = JsonConvert.SerializeObject(data);

            using (var webClient = new WebClient())
            {
                webClient.Headers[HttpRequestHeader.ContentType] = "application/json";
                var responseJson = webClient.UploadString("http://192.168.1.109:3000/api/command", "POST", json);
                ApiResponse response = JsonConvert.DeserializeObject<ApiResponse>(responseJson);
                Console.WriteLine(response.Message);
            }
        }



        private void button1_Click_1(object sender, EventArgs e)
        {
            
            SendButtonCommand("button1");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SendButtonCommand("button2");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            
            SendButtonCommand("button3");
        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            SendButtonCommand("button4");
        }
    }




}

