import matplotlib.pyplot as plt
import numpy as np

class Graph():
        def __init__(self, labels, sizes ,cost, rent):
                self.labels = labels
                self.sizes = sizes
                self.cost = cost
                self.rent = rent
        
        def barChart(self):
                yPos = np.arange(len(self.labels))

                fig1, ax = plt.subplots(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

                plt.bar(yPos, self.sizes, align='center', alpha=0.5)
                plt.xticks(yPos, self.labels)
                plt.ylabel('Landed (%)')
                plt.title('Number of times landed on')

                plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='x-small')

                plt.show()

        def lineChart(self):
                fig, ax = plt.subplots(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

                colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] * 4

                i = 0
                for cost in self.cost:
                        plt.scatter(cost, self.rent[i], color=colors[i], label=self.labels[i])
                        i += 1
                
                plt.axis([0, 500, 0, 60])

                # for i, txt in enumerate(self.labels):
                #         ax.annotate(txt, (self.cost[i], self.rent[i]))
                ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

                plt.show()
