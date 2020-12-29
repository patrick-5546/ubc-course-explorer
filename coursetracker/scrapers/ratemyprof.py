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
    
    def professor_info(self, ProfessorName):
        self.indexnumber = self.GetProfessorIndex(ProfessorName)
        return self.GetProfessorInfo()

    def GetProfessorIndex(self, ProfessorName):  # function searches for professor in list
        for i in range(0, len(self.professorlist)):
            if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                return i
        return False  # Return False is not found

    def GetProfessorInfo(self):  # print search professor's name and RMP score
        if self.indexnumber == False:
            return {}
        else:
            return self.professorlist[self.indexnumber]

ubc = RateMyProfScraper(1413)  # 1413 is the school ID for UBC on Rate My Prof
