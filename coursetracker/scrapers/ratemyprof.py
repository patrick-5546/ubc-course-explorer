'''Adapted from https://github.com/Rodantny/Rate-My-Professor-Scraper-and-Search'''


import json
import math
import requests


class RateMyProfScraper:
    '''
    Available data for each prof (eg. Robert Gateman):
    {
    'tDept': 'Economics',
    'tSid': '1413',
    'institution_name': 'University of British Columbia',
    'tFname': 'Robert',
    'tMiddlename': '',
    'tLname': 'Gateman',
    'tid': 13305,
    'tNumRatings': 1061,
    'rating_class': 'good',
    'contentType': 'TEACHER',
    'categoryType': 'PROFESSOR',
    'overall_rating': '3.7'
    }
    '''
    def __init__(self, schoolid):
        self.UniversityId = schoolid
        self.professorlist = self.create_professor_list()
        self.indexnumber = False

    def create_professor_list(self):
        '''Creates List object that include basic information on all Professors from the IDed University.'''
        tempprofessorlist = []
        num_of_prof = self.GetNumOfProfessors(self.UniversityId)
        num_of_pages = math.ceil(num_of_prof / 20)
        i = 1
        while (i <= num_of_pages):  # the loop insert all professor into list
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(i) +
                                "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=" +
                                "schoolId&sid=" + str(self.UniversityId))
            temp_jsonpage = json.loads(page.content)
            temp_list = temp_jsonpage['professors']
            tempprofessorlist.extend(temp_list)
            i += 1
        return tempprofessorlist

    def GetNumOfProfessors(self, id):
        '''Function returns the number of professors in the university of the given ID.'''
        # get request for page
        page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+" +
                            "asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(id))
        temp_jsonpage = json.loads(page.content)
        num_of_prof = temp_jsonpage['remaining'] + 20  # get the number of professors
        return num_of_prof

    def update_rmp_data(self):
        with open('coursetracker/scrapers/local_data/rmp_ubc_profs_list.txt', 'w') as outfile:
            json.dump(self.professorlist, outfile)


def get_profs_info(profsList):
    '''Returns the rating and number of ratings for each professor in a list

    Inputs:
        - profsList - list of professor names to get info for
    '''
    ubcProfs = []
    try:
        with open('coursetracker/scrapers/local_data/rmp_ubc_profs_list.txt') as json_file:
            ubcProfs = json.load(json_file)
    except OSError:
        return None

    profs_info = []
    for prof in profsList:
        for profInfo in ubcProfs:
            if prof == profInfo['tFname'] + ' ' + profInfo['tLname'] and profInfo['tNumRatings'] != 0:
                profs_info.append([prof, profInfo['overall_rating'], profInfo['tNumRatings']])
    return profs_info
