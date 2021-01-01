import requests, json, math

# Adapted from https://github.com/Rodantny/Rate-My-Professor-Scraper-and-Search

# To use in other files, import ratemyprof and call ratemyprof.ubc.professor_info("FirstName LastName")
# If professor not found, returns empty dictionary
#
# Return example for Robert Gateman:
# {
#   'tDept': 'Economics',
#   'tSid': '1413',
#   'institution_name': 'University of British Columbia',
#   'tFname': 'Robert',
#   'tMiddlename': '',
#   'tLname': 'Gateman',
#   'tid': 13305,
#   'tNumRatings': 1061,
#   'rating_class': 'good',
#   'contentType': 'TEACHER',
#   'categoryType': 'PROFESSOR',
#   'overall_rating': '3.7'
# }
class RateMyProfScraper:

    def __init__(self, schoolid):
        self.UniversityId = schoolid
        self.professorlist = self.create_professor_list()
        self.indexnumber = False
        self.file_to_save_rmp_data = 'coursetracker/scrapers/rmp_ubc_profs_list.txt'

    def create_professor_list(self):  # creates List object that include basic information on all Professors from the IDed University
        tempprofessorlist = []
        num_of_prof = self.GetNumOfProfessors(self.UniversityId)
        num_of_pages = math.ceil(num_of_prof / 20)
        i = 1
        while (i <= num_of_pages):# the loop insert all professor into list
            page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                self.UniversityId))
            temp_jsonpage = json.loads(page.content)
            temp_list = temp_jsonpage['professors']
            tempprofessorlist.extend(temp_list)
            i += 1
        return tempprofessorlist

    def GetNumOfProfessors(self, id):  # function returns the number of professors in the university of the given ID.
        page = requests.get(
            "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                id))  # get request for page
        temp_jsonpage = json.loads(page.content)
        num_of_prof = temp_jsonpage[
                            'remaining'] + 20  # get the number of professors
        return num_of_prof
    
    def update_rmp_data(self):
        with open(self.file_to_save_rmp_data, 'w') as outfile:
            json.dump(self.professorlist, outfile)


ubcProfs = RateMyProfScraper(1413)  # 1413 is the school ID for UBC on Rate My Prof
