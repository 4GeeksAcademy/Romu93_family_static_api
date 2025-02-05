
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{"id": 1,
                          "name": "John",
                          "last_name": last_name,
                          "age": 33,
                          "lucky_number": [7, 13, 22]},

                          {"id": 5,
                           "name": "Jane ",
                           "last_name": last_name,
                           "age": 35,
                           "lucky_number": [10, 14, 3]},

                          {"id": 9,
                           "name": "Jimmy",
                           "last_name": last_name,
                           "age": 5,
                           "lucky_number": [1]}]



    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)

        return self._members

    def delete_member(self, member_id):
        # fill this method and update the return
        the_members = []
        for member in self._members:
            if member["id"] != member_id:
                the_members.append(member)
        return the_members

    def get_member(self, member_id):
        # fill this method and update the return
        the_member = []
        for member in self._members:
            if member["id"] == member_id:
                the_member.append(member)
        return the_member


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
