using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WinMuseEEG.Models;

namespace WinMuseEEG
{
	class EegEventArgs: EventArgs
	{
		public Eeg Eeg { get; set; }
	}
}
