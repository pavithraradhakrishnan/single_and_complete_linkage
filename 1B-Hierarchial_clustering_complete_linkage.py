
import math
import csv

with open("input.csv", encoding='utf-8-sig') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data = [data for data in rows]
input_data = []
print("Please look for the brackets in the resultant clusters to see how clustering is done")
print("###################CLUSTERING RESULTS FOR COMPLETE LINKAGE##############################")
for x in range(len(data)):
    ins = []
    for y in range(3):
        ins.append(int(data[int(x)][int(y)]))
    #print("ins",ins)
    input_data.append([ins])
############This function is used tocompute the euclidiean distance between the points##############
def calculate_euclidian_distance(pt1,pt2):
    squares = [(p - q) ** 2 for p, q in zip(pt1, pt2)]
    return sum(squares) ** .5

def single_linkage(clusters,n):
    while len(clusters) is not n:
        clusters_length = len(clusters)
        #print("clusters length", clusters_length)
        min_dist = clust1 = clust2 = math.inf

        for cluster_no,cluster in enumerate(clusters[:clusters_length]):
           #print("cluster2", cluster2)
            for cluster2_no, cluster2 in enumerate(clusters[(cluster_no + 1):]):
                max_furthest_dist = - 1
                for pt_cluster_no, pt in enumerate(cluster):

                    for pt2_cluster_no,pt2 in enumerate(cluster2):
                        #print("pt,pt2",pt,pt2)
                        current_dist = calculate_euclidian_distance(pt, pt2)
                        #print("type pt",type(pt))
                        ###### check if the max_furthest_distance has the maximum dist between the clusters
                        if(max_furthest_dist <current_dist):
                            max_furthest_dist = current_dist
                if max_furthest_dist < min_dist:
                    min_dist = max_furthest_dist
                    clust1 = cluster_no
                    clust_pt = pt
                    clust_pt2 = pt2
                    clust2 = cluster2_no + cluster_no + 1

        print("merge at clusters ", clust_pt, "(id:", clust1, ")" "<--> ", clust_pt2, "(id:", clust2, ")",
              "at distance", min_dist)
        #print("merge at clusters " ,clust1 , "<--> " ,  clust2 , "at distance" , min_dist)
        #print("clust1",clust1)
        #print("clust2",clust2)
        clusters[clust1].extend(clusters[clust2])
        clusters.pop(clust2)
        print("The length of the clusters now are", len(clusters))
        print("The resultant clusters now are", clusters)
    return (clusters)

def clustering(input,n):
    clusters_data = []
    #print("input_data",input_data)
    result = single_linkage(input,n)
    return result
clustering(input_data,1)











