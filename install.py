import sys, subprocess; 

subprocess.run([sys.executable, '-m', 'pip', 'install', 
                'numpy', 'scipy', 'matplotlib', 'seaborn', 'pandas', 
                'quarto', 'jupyter', 'jupyterlab'])
