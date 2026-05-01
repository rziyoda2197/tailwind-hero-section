import tailwindcss

# Hero section uchun ma'lumotlar
hero_data = {
    "title": "SaaS Landing Page",
    "description": "SaaS uchun ideal landing sahifa",
    "button_text": "Batafsil",
    "background_image": "https://picsum.photos/2000/1000"
}

# Hero sectionni yaratish
def create_hero_section(hero_data):
    html = f"""
    <section class="bg-cover bg-center h-screen" style="background-image: url({hero_data['background_image']})">
        <div class="container mx-auto p-4 md:p-6 lg:p-12 flex justify-center items-center h-full">
            <div class="text-white max-w-md">
                <h1 class="text-3xl md:text-5xl font-bold mb-4">{hero_data['title']}</h1>
                <p class="text-lg md:text-xl mb-8">{hero_data['description']}</p>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">{hero_data['button_text']}</button>
            </div>
        </div>
    </section>
    """
    return html

# Hero sectionni chiqarish
print(create_hero_section(hero_data))
