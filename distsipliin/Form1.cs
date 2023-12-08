using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace distsipliin
{
    public partial class Form1 : Form
    {
        public int timer = 0;
        public Form1()
        {
            
            InitializeComponent();
            label3.Text = timer.ToString();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text=="t"){
                Console.WriteLine("Hello World"); }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {
        }

        public void label3_Click(object sender, EventArgs e)
        {
            

        }
        

    }
}
