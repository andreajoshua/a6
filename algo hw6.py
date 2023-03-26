#!/usr/bin/env python
# coding: utf-8

# In[7]:


import altair as alt
import pandas as pd

mbta = pd.read_excel(r'/Users/andreajoshua/Downloads/MBTA_Line_and_Stop(1).xlsx')
print(mbta.head())


# axis_labels = ("datum.label == 'time_period_01' ? 'VERY_EARLY_MORNING': datum.label == 'time_period_02' ? 'EARLY_AM : 'Frequent'")
# 
# x = alt.X("time_period_id",axis=alt.Axis(labelExpr=axis_labels))
# 
# Replace the given axis_labels with the other time_period_0x labels, it should work.

# In[52]:


axis_labels = ("datum.label == 'time_period_01' ? 'VERY_EARLY_MORNING': datum.label == 'time_period_02' ? 'EARLY_AM': datum.label == 'time_period_03' ? 'AM_PEAK': datum.label == 'time_period_04' ? 'MIDDAY_BASE': datum.label == 'time_period_05' ? 'MIDDAY_SCHOOL': datum.label == 'time_period_06' ? 'PM_PEAK': datum.label == 'time_period_07' ? 'EVENING': datum.label == 'time_period_08' ? 'LATE_EVENING': datum.label == 'time_period_09' ? 'NIGHT': datum.label == 'time_period_10' ? 'OFF_PEAK':'OFF_PEAK'")

new_x = alt.X("time_period_id",axis=alt.Axis(title="Time Period", labelExpr=axis_labels))

brush = alt.selection_interval(
    encodings=['x'] 
)

service = alt.Chart(mbta).mark_point().add_selection(
    brush
).encode(
    alt.X('number_service_days:Q', title='Number of service days'),
    alt.Y('total_ons:Q', title='Totals on'),
     color='route_name',
      tooltip=['time_period_id', 'total_ons']
).properties(
    width=650,
    height=50,
    title=alt.TitleParams(text="Number of service days v Total Ons", fontSize=16, subtitle="Source: MBTA data")
)

hover = alt.selection_single(
    on='mouseover', 
    nearest=True,    
    empty='none'     
)

click = alt.selection_multi(
    empty='none'
)

base = service.transform_filter(
    hover | click
)

alt.layer(
    service.add_selection(hover).add_selection(click),
    base.mark_point(size=100, stroke='firebrick', strokeWidth=1),
    base.mark_text(dx=4, dy=-8, align='right', stroke='white', strokeWidth=2).encode(text='Title:N'),
    base.mark_text(dx=4, dy=-8, align='right').encode(text='Title:N'),
    data=mbta
).properties(
    width=600,
    height=450
)

brush2 = alt.selection_interval(
    encodings=['x'] 
)

period = alt.Chart(mbta).mark_line().add_selection(
    brush2
).encode(
    x=new_x,
    y=alt.Y('average_ons', 
            axis=alt.Axis(title='Average ons')),
    color=alt.Color('route_name', scale=alt.Scale(range=['#9ecae1', 'green', '#fdd0a2', 'red'])),
     tooltip=['time_period_id', 'average_ons'],
    opacity=alt.condition(brush, alt.value(0.75), alt.value(0.05))
).properties(
    width=650,
    height=400,
    title=alt.TitleParams(text="Average ons by time period", fontSize=16, subtitle="Source: MBTA data")
)

alt.vconcat(service, period).properties(spacing=5)


# # Caption for line chart
# 
# This line chart plots the average ons (y-axis) over time (x-axis). The average ons represents how many people get on the respective T-line, which is differentiated by color in the graph. As someone who lives in Boston and regularly takes the MBTA, there were a lot of interesting insights I gained from this chart. I have never taken the blue line before so I'm surprised by how many people take it, especially at night. The fact that the red line is so popular is also interesting, mainly because I assumed there were less train commuters in the Cambridge area and other popular red-line destinations. Another interesting observation of the plot is how the PM peak is noticeably larger than the AM peak. This must mean that people who are traveling during the night aren't necessarily working a 9-5 schedule, which makes sense given how many students are in Boston. 

# # Caption for scatter plot
# A caption for each visualization to explain what it is plotting and the most interesting insights/observations.
# 
# This scatter chart plots the total ons (y-axis) by the number of service days (x-axis). One interesting observation from this chart is how many service days the red line and green line have in comparison to the other lines. After charting the line plot, this makes much more sense because of the sheer amount of passengers the red line and green line has in comparison to the other two. Something that would be interesting to consider in future graphs is whether these service days have increased, decreased, or stayed the same over time. Another interesting observation is how the orange line has some of the most service days in comparison to the other lines, but has few passengers relative to the other ones (which we can see in the line chart).
# 

# # Pop-Out Effect
# The pop-out effect I chose was contrast. We learned in class how our eyes see with rods and cones and how red is the easiest to see compared to green and blue. Since I had to apply it to both red and green, I didn't change the color of red, but I chose a green with a deeper saturation so it stood out. Then I changed the blue and orange lines to pastel colors so the red and green really popped out. I chose this effect because I thought it would be distracting to choose a different kind of line, for example a dotted line, or changing it in a significant way in general. That would have probably led the viewers to believe there's something inherently different between the data, when there isn't. Using color was also a good way for me to see how glaring red can be, so I can apply that knowledge to our project visualizations.

# In[ ]:




