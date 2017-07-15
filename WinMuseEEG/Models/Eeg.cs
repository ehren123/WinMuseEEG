using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinMuseEEG.Models
{
	public class Eeg
	{
		//Tp9 Fp1, Fp2, TP10
		public float Tp9 { get; set; }
		public float Fp1 { get; set; }
		public float Fp2 { get; set; }
		public float Tp10 { get; set; }

		public Eeg(float tp9, float fp1, float fp2, float tp10)
		{
			Tp9 = tp9;
			Fp1 = fp1;
			Fp2 = fp2;
			Tp10 = tp10;
		}
	}
}
