from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice,Person,Group,Membership

##############################
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields= ['pub_date','question_text']
	fieldsets = [
	('question fill', {'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
	#list_display = ('question_text', 'pub_date')
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	#list_filter = ['question_text']
	list_filter = ['pub_date']
	search_fields = ['question_text']
class MembershipInline(admin.TabularInline):
	model = Membership
	extra = 1
class PersonAdmin(admin.ModelAdmin):
	inlines = (MembershipInline,)
class GroupAdmin(admin.ModelAdmin):
	inlines = (MembershipInline,)

admin.site.register(Question,QuestionAdmin)
admin.site.register(Person, PersonAdmin)
#admin.site.register(Group)
#admin.site.register(Person)
#admin.site.register(Membership)
admin.site.register(Group, GroupAdmin)
