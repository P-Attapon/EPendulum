import numpy as np
from matplotlib.patches import Arrow
from matplotlib import pyplot as plt
from tqdm import tqdm
import pickle


file = open('pendulumSim', 'rb')
solE0 = pickle.load(file)
solE10 = pickle.load(file)
solPerturb = pickle.load(file)

sin, cos = np.sin, np.cos

fig, ax =  plt.subplots(1)

def animate(plot_E,t_arr,theta1_arr,theta2_arr,save_path):
    for i in tqdm(range(len(t_arr))):
        ax.clear()

        x1 = sin(theta1_arr[i])
        y1 = -cos(theta1_arr[i])

        x2 = sin(theta1_arr[i]) + sin(theta2_arr[i])
        y2 = -cos(theta1_arr[i]) - cos(theta2_arr[i])

        ax.scatter(x1,y1,color = "blue")
        ax.scatter(x2,y2,color = "blue")

        ax.scatter(x1, y1, color="blue")
        ax.scatter(x2, y2, color="red")

        # plot string
        ax.plot([0, x1], [0, y1], "-", color="black")
        ax.plot([x1, x2], [y1, y2], "-", color="black")
        if plot_E:
            arrow = Arrow(0, 0, 0, sin(t_arr[i]), width=0.05, color="red")
            ax.add_patch(arrow)
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)

        plt.savefig(save_path  + f"frame {i}")


animate(plot_E=True, t_arr = solE10[0], theta1_arr=solE10[1], theta2_arr = solE10[2],
        save_path = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\E10\\"
)

animate(plot_E=True, t_arr = solPerturb[0], theta1_arr=solPerturb[1], theta2_arr = solPerturb[2],
        save_path = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\EPerturb\\"
)