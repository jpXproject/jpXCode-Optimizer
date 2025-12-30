import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import threading
import winreg
from ai_engine import AIRecommendationEngine

class OptimizerApp:
    def __init__(self, root):
        self.root = root
        root.title("jpXCode Optimizer :: FINAL")
        root.geometry("1100x700")

        self.create_ui()
        self.update_system_monitor()
        self.update_process_table()

    # ================= UI =================

    def create_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        self.tab_monitor = ttk.Frame(notebook)
        self.tab_process = ttk.Frame(notebook)
        self.tab_ai = ttk.Frame(notebook)

        notebook.add(self.tab_monitor, text="📊 System Monitor")
        notebook.add(self.tab_process, text="⚙ Task Manager")
        notebook.add(self.tab_ai, text="🤖 AI Assistant")

        self.create_monitor_tab()
        self.create_process_tab()
        self.create_ai_tab()

    # ================= SYSTEM MONITOR =================

    def create_monitor_tab(self):
        cols = ("Metric", "Value", "Status")
        self.sys_table = ttk.Treeview(self.tab_monitor, columns=cols, show="headings")
        for c in cols:
            self.sys_table.heading(c, text=c)
            self.sys_table.column(c, anchor="center", width=200)
        self.sys_table.pack(fill="x", pady=20)

        self.items = {
            "CPU": self.sys_table.insert("", "end", values=("CPU Usage", "-", "-")),
            "RAM": self.sys_table.insert("", "end", values=("RAM Usage", "-", "-")),
            "DISK": self.sys_table.insert("", "end", values=("Disk Usage", "-", "-")),
        }

    def update_system_monitor(self):
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("C:\\").percent

        self._update_row("CPU", cpu)
        self._update_row("RAM", ram)
        self._update_row("DISK", disk)

        self.root.after(1000, self.update_system_monitor)

    def _update_row(self, key, val):
        status = "OK" if val < 60 else "WARN" if val < 80 else "HIGH"
        self.sys_table.item(
            self.items[key],
            values=(f"{key} Usage", f"{val:.1f} %", status)
        )

    # ================= PROCESS TABLE =================

    def create_process_tab(self):
        cols = ("PID", "Process", "CPU %", "RAM %")
        self.proc_table = ttk.Treeview(self.tab_process, columns=cols, show="headings")
        for c in cols:
            self.proc_table.heading(c, text=c)
            self.proc_table.column(c, anchor="center")
        self.proc_table.pack(fill="both", expand=True)

    def update_process_table(self):
        self.proc_table.delete(*self.proc_table.get_children())
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                self.proc_table.insert(
                    "",
                    "end",
                    values=(
                        p.info['pid'],
                        p.info['name'][:30],
                        f"{p.info['cpu_percent']:.1f}",
                        f"{p.info['memory_percent']:.1f}"
                    )
                )
            except:
                pass
        self.root.after(2000, self.update_process_table)

    # ================= AI ASSISTANT =================

    def create_ai_tab(self):
        self.ai_output = tk.Text(self.tab_ai, height=20)
        self.ai_output.pack(fill="both", expand=True, padx=10, pady=10)

        btn = ttk.Button(
            self.tab_ai,
            text="🧠 Analyze System with AI",
            command=self.run_ai
        )
        btn.pack(pady=10)

    def run_ai(self):
        def task():
            try:
                self.ai_output.delete(1.0, tk.END)
                self.ai_output.insert(tk.END, "AI analyzing system...\n\n")

                snapshot = self.get_snapshot()
                ai = AIRecommendationEngine()
                result = ai.analyze(snapshot)

                self.ai_output.insert(tk.END, result)

            except Exception as e:
                messagebox.showerror("AI Error", str(e))

        threading.Thread(target=task, daemon=True).start()

    # ================= SNAPSHOT =================

    def get_snapshot(self):
        processes = []
        for p in psutil.process_iter(['name','cpu_percent','memory_percent']):
            try:
                processes.append(
                    f"{p.info['name']} CPU:{p.info['cpu_percent']} RAM:{p.info['memory_percent']}"
                )
            except:
                pass

        return {
            "cpu": psutil.cpu_percent(interval=None),
            "ram": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("C:\\").percent,
            "startup": self.count_startup(),
            "processes": "\n".join(processes[:5])
        }

    def count_startup(self):
        count = 0
        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Run"
            )
            count = winreg.QueryInfoKey(key)[1]
            winreg.CloseKey(key)
        except:
            pass
        return count

# ================= RUN =================

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimizerApp(root)
    root.mainloop()
