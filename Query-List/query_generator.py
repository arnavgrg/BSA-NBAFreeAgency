query_list = []

def query_generator(player_info):
    '''
    Generate a list of similar google search queries
    for each player being considered. 

    player_info is a dictionary where each player has an 
    associated old team and new team that will be used to
    create a list of queries. 
    '''
    global query_list
    num_questions = 10
    for i in range(num_questions):
        pass
    f = open("query_list.csv","w+")
    #f.write("Blank")
    f.close()
    return 

def main():
    player_info = {}
    query_generator(player_info)

if __name__ == "__main__":
    main()