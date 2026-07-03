from app.llm.gemini import get_gemini_response


def career_agent(data):

    if data.type == "career":

        prompt = f"""
You are a senior AI Career Mentor.

Current Skills:
{data.current_skills}

Career Goal:
{data.goal}

Provide:

## Skill Gap
What skills are missing?

## Learning Order
What should the user learn next?

## Recommended Projects
Suggest 3 portfolio projects.

## Resume Tips
How can the user improve their resume?

## Interview Preparation
What should the user focus on?

Keep the answer under 600 words.
Use Markdown headings.
Be practical and specific.
"""
        return get_gemini_response(prompt)

    else:

        prompt = f"""
You are an expert AI Career Mentor.

Current Skills:
{data.current_skills}

Career Goal:
{data.goal}

Duration:
{data.duration}

Create a practical learning roadmap.

Rules:
- Divide the plan week by week.
- Each week should include:
    - Topics to learn
    - One mini project
    - Expected outcome
- Keep the response under 700 words.
- Focus on practical skills rather than theory.
- Assume the user is preparing for internships.
- Format using Markdown headings and bullet points.

End with:
'Final Portfolio Projects' and suggest 3 projects the user should build.
"""
        return get_gemini_response(prompt)