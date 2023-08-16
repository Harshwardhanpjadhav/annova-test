# Importing Library
from scipy.stats import f_oneway


# Function to perform f_oneway ANOVA test
def f_oneway_test(data,predictor_list,target,alpha):
    '''
    This function takes in a dataframe, a list of predictor, a target variable and a significance level
    and returns a list of predictor that are correlated with the target variable
    return: 

    Input: data: dataframe 
            predicator_list: list of predictor (Independent Features)
            target: target variable (Dependent Feature)
            alpha: significance level
    Output: 
        return selected columns in list
    '''
    selected_columns = []
    for predictor in predictor_list:
        cat_vs_num = data.groupby(predictor)[target].apply(list)
        f_statistic, p_value = f_oneway(*cat_vs_num)

        if (p_value < alpha):
                print(predictor, 'is correlated with', target, '| P-Value:', p_value)
                selected_columns.append(predictor)
        else:
            print(predictor, 'is NOT correlated with', target, '| P-Value:', p_value)
    print("--------------Selected Features------------")
    return selected_columns