## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Data Visualization with Data Studio
- This project will let you show off your skills making visualizations using datasets stored on BigQuery! Your code review submission for this week will be a Data Studio report; you won't be making a GitHub repository.

### Setup Project
- In Google's Data Studio, start with a new blank report.

### Get the Data:
We will be using one of BigQuery's publicly available datasets. To use it:
1. In your new Data Studio report, click 'Add Data' then 'BigQuery' as usual
2. In the window that opens, click 'Public Datasets'
3. With that selected, in the 'Billing Project' column select your project
4. A column should appear to the right with a list of BigQuery's publicly available datasets. Select 'stackoverflow'.
5. Another column should appear to the right of that with the tables available in that dataset. Select 'posts_questions', then click the 'Add' button to add the data to your report.

### Instructions:
#### Create the Charts
- Create a bar chart using 'tags' as the dimension and 'record count' as the metric.
- Make a chart based on the one above, but drill down, using 'score' as the breakdown dimension.
- Using the first chart again, make a stacked bar chart grouping posts by tag, broken down within that category to show the 'favorite_count'. Add a drop-down that would allow a user to show only answers that aren't 'null' or 0.
- Create a line chart showing the number of posts over the entire range of available dates.
- Make a pie chart that groups the post by 'answer_count'. Add an advanced filter to it that allows a user to only show posts that have between 1-8 answers.

#### Explain the Charts
- Under each chart, add a text box. Write a few sentences explaining what this chart is showing (i.e., "This chart shows the count of the posts grouped by tag") and what information about the data your user can see from the chart (i.e. "Posts about C++ are the lease common".)
    -If writing is difficult for you and you need accommodation, you can send your teacher an audio file instead, or request a meeting on your code review submission form.

#### Share the Report
- In the top toolbar of Data Studio, click the dropdown arrow on the 'Share' button, and select 'Get Report Link'. Please add this to your code review submission form, rather than the usual link to a GitHub repository.

### Accepting Criteria
Your submitted report should:
- Include the charts outlined above.
- Include brief descriptions of each chart.

#### Three Point Bonus:
Use one of BigQuery's publicly available dataset to make a geospacial chart. 