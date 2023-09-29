## About  

``` 
Clustering of Data Through Hierarchical Clustering (Ward, Centroid, and Average) along with K-Means Clustering to better understand market segments for EastWest Airlines. 

Reports are Outlined as Summary, Dendrogram, Scatterplot Matrix, and Parallel Coord Plots

Note Parallel Coord Plots listed within ParallelPlots.txt
```

## Goal  

``` 
Identify clusters of passengers with similar characteristics to target different segments for different types of mileage offers

```

## Results 

```
Cluster Summary (ward):
               ID#         Balance   Qual_miles   cc1_miles   cc2_miles   cc3_miles   Bonus_miles   Bonus_trans   Flight_miles_12mo   Flight_trans_12   Days_since_enroll     Award?
Cluster
1        2269.372093   68876.581395    23.255814    1.139535    2.348837    1.000000  14689.837209     17.534884          582.627907          2.209302         3968.930233  0.395349
2        2258.335439   50456.873333   177.163509    1.397193    1.000000    1.000000   6866.912982      8.351579          323.272632          0.980351         3673.865263  0.279298
3        1497.604167  148606.020833   393.125000    2.666667    1.000000    1.000000  42401.354167     32.541667         6683.468750         18.572917         5040.406250  0.822917
4        1365.994059  131981.929703    32.334653    3.909901    1.000000    1.048515  43850.836634     18.530693          249.277228          0.812871         5292.138614  0.583168
Cluster Summary (centroid):
               ID#        Balance   Qual_miles   cc1_miles   cc2_miles   cc3_miles   Bonus_miles   Bonus_trans   Flight_miles_12mo   Flight_trans_12   Days_since_enroll     Award?
Cluster
1        3128.000000  1.319995e+05   347.000000    2.500000    1.000000    1.000000  65634.250000     69.250000        19960.000000         49.250000         2200.250000  1.000000
2        1664.866667  1.380614e+05    78.800000    3.466667    1.000000    4.066667  93927.866667     28.066667          506.666667          1.600000         4613.866667  0.533333
3        2015.455893  7.288966e+04   144.193013    2.054034    1.014577    1.000754  16806.654184     11.476753          439.180699          1.319176         4117.825333  0.368937
4         279.000000  1.704838e+06     0.000000    1.000000    1.000000    1.000000  17108.000000     32.000000         4823.000000         23.000000         7283.000000  1.000000
Cluster Summary (average):
               ID#        Balance   Qual_miles   cc1_miles   cc2_miles   cc3_miles   Bonus_miles   Bonus_trans   Flight_miles_12mo   Flight_trans_12   Days_since_enroll     Award?
Cluster
1        3128.000000  1.319995e+05   347.000000    2.500000    1.000000    1.000000  65634.250000     69.250000        19960.000000         49.250000         2200.250000  1.000000
2        1664.866667  1.380614e+05    78.800000    3.466667    1.000000    4.066667  93927.866667     28.066667          506.666667          1.600000         4613.866667  0.533333
3        2015.455893  7.288966e+04   144.193013    2.054034    1.014577    1.000754  16806.654184     11.476753          439.180699          1.319176         4117.825333  0.368937
4         279.000000  1.704838e+06     0.000000    1.000000    1.000000    1.000000  17108.000000     32.000000         4823.000000         23.000000         7283.000000  1.000000

Cluster Summary for 4 Clusters:
                 ID#         Balance   Qual_miles   ..
Cluster_4                                           ..
0          2239.866478   42759.036305   104.981444  ..
1          1727.437500  193026.631250   802.787500  ..
2          1638.119703  115521.840892   138.614870  ..
3          1664.866667  138061.400000    78.800000  ..

```

