using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SharpOSC;
using WinMuseEEG.Models;

namespace WinMuseEEG
{
	class EegProcessor
	{
		public Stack<Eeg> Eegs { get; private set; }

		public void Push(Eeg eeg)
		{
			Eegs.Push(eeg);
		}

		public Eeg Pop()
		{
			return Eegs.Pop();
		}

		public void PushOscMessage(OscMessage oscMessage)
		{
			string data = string.Empty;
		}
	}
}
