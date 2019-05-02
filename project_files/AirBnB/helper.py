import pandas as pd
import numpy as np

from sklearn.decomposition import PCA

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns


def scree_plot(pca):
    '''
    Creates a scree plot associated with the principal components 
    
    INPUT: pca - the result of instantian of PCA in scikit learn
            
    OUTPUT:
            None
    '''
    num_components=len(pca.explained_variance_ratio_)
    ind = np.arange(num_components)
    vals = pca.explained_variance_ratio_
 
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)
    cumvals = np.cumsum(vals)
    ax.bar(ind, vals)
    ax.plot(ind, cumvals)
    for i in range(num_components):
        ax.annotate(r"%s%%" % ((str(vals[i]*100)[:4])), (ind[i]+0.2, vals[i]), va="bottom", ha="center", fontsize=12)
 
    ax.xaxis.set_tick_params(width=0)
    ax.yaxis.set_tick_params(width=2, length=12)
 
    ax.set_xlabel("Principal Component")
    ax.set_ylabel("Variance Explained (%)")
    plt.title('Explained Variance Per Principal Component')
    

      
#Modifeid version of function from helper_functions.py in MiniPCA 
def pca_results_rng(full_dataset, pca,dim_rng,pltpca=False):
    '''
    Create a DataFrame of the PCA results
    Includes dimension feature weights and explained variance
    Visualizes the PCA results
    
    input: 
    full_dataset: is the full dataset that was transformed
    pca: is the fit_transformed pca
    dim_rng: list of size to of the first and last dimention to be displayed (i.e [1,5] denotes Dimentions 1 through Dimention 5)
    pltpca (boolean) = Display graph of
    
    '''
    dim_rng[0] = dim_rng[0] - 1  #because first dimention is at index 0
    
    # Dimension indexing
    dimensions = ['Dimension_{}'.format(i) for i in range(1, len(pca.components_)+1)]
    dim = dimensions[dim_rng[0]:dim_rng[1]]
    
    # PCA components
    components = pd.DataFrame(np.round(pca.components_, 4), columns = full_dataset.keys())
    components.index = dimensions
    comp = components.iloc[dim_rng[0]:dim_rng[1]]

    # PCA explained variance
    ratios = pca.explained_variance_ratio_.reshape(len(pca.components_), 1)
    variance_ratios = pd.DataFrame(np.round(ratios, 4), columns = ['Explained Variance'])
    variance_ratios.index = dimensions
    vr = variance_ratios.iloc[dim_rng[0]:dim_rng[1]]

    if pltpca == True:
        fig, ax = plt.subplots(figsize = (20,8))

        # Plot the feature weights as a function of the components
        comp.plot(ax = ax, kind = 'bar');
        ax.set_ylabel("Feature Weights")
        ax.set_xticklabels(dim, rotation=0)

        # Display the explained variance ratios
        for i, ev in enumerate(pca.explained_variance_ratio_):
            if int(i) >= dim_rng[0] and int(i) < dim_rng[1]:
                ax.text(i-dim_rng[0], ax.get_ylim()[1], "Explained Variance\n%.4f"%(ev))

    # Return a concatenated DataFrame
    return pd.concat([vr, comp], axis = 1)
