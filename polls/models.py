from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



'''
*** Coronavirus-related questions ***
(from https://news.gallup.com/poll/308222/coronavirus-pandemic.aspx)

1. What's your impression of the coronavirus situation in the U.S. today? Is it -- getting a lot worse,
getting a little worse, staying about the same, getting a little better or getting a lot better?

2. Which of these do you think is better advice right now for people who do not have symptoms of coronavirus and
are otherwise healthy -- to stay home as much as possible to avoid contracting or spreading the coronavirus or to
lead their normal lives as much as possible and avoid interruptions to work and business?

3. Next, thinking about everything you've done in the past 24 hours, which of the following comes closest
to describing your in-person contact with people outside your household?

4. There are some things people may do because of their concern about the coronavirus. For each one of the following,
please indicate if this is something you have done, are considering doing or have not considered in the past 7 days.

5. In the past 24 hours, have you visited any of the following places? Please select all that apply.

6. If there were no government restrictions and people were able to decide for themselves about being out in public,
how soon would you return to your normal day-to-day activities -- right now, after the number of new cases declines
significantly in [the U.S./your state], after there are no new cases in [the U.S./your state] for a period of time
or after a coronavirus vaccine is developed?

7. How long can you follow social distancing practices and business/school closures before experiencing significant
financial hardship?

8. How long can you follow social distancing practices and business/school closures before your emotional or
mental health suffers?

9. In your household, which of the following statements best describes the current financial situation: you are saving
a lot, you are saving a little, you are just managing to make ends meet, you are having to draw on savings or you are
running into debt?

10. If you had to choose, which of the following do you think is more important -- protecting people's medical privacy,
even if it makes it harder to limit the spread of the coronavirus, or preventing the spread of the coronavirus, even if
that means people have to reveal sensitive medical information?

'''
