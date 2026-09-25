import html, json

# ---------- MTA line colors (the brand) ----------
L = {
    "red": "#EE352E", "green": "#00933C", "blue": "#0039A6", "orange": "#FF6319",
    "yellow": "#FCCC0A", "purple": "#B933AD", "grey": "#808183", "brown": "#996633",
    "lime": "#6CBE45", "teal": "#00A1DE",
}

DAYS = [
 dict(n=1, dow="Friday", date="25 September", theme="Landing", line="EWR", color=L["grey"], area="Hell's Kitchen",
      intro="Straight off Dublin, then Cleveland. The evening is for arriving. Nothing else.",
      plan=[("7:20pm","UA 1274 leaves Cleveland."),("8:30pm","Car on its way to Newark. Terminal C."),("8:57pm","Lands. Bags, twenty to thirty minutes."),("9:30pm","Car home, forty-five minutes at that hour."),("10:30pm","Home. Champagne on the table, charcuterie, flowers. No plan for the morning.")],
      food=("Champagne and charcuterie","At home. The first meal is the one with nothing to get to."),
      swap="If the flight's late, the champagne waits."),
 dict(n=2, dow="Saturday", date="26 September", theme="West Side: the Chelsea galleries, then the Joyce", line="A", color=L["blue"], area="Chelsea",
      intro="The Joyce is at 8th and 19th, so the whole day lives within ten blocks of the theater. New ground this time: the gallery district, not the museum.",
      plan=[("Morning","No alarm. Coffee and papers."),("12:30pm","Late brunch in Chelsea. Somewhere on 9th or 10th Ave, close to the galleries."),("1:45pm","The Chelsea galleries, W 20th to 26th between 10th and 11th. Zwirner, Pace, Gagosian, Hauser & Wirth, and thirty smaller ones. All free, Saturday is the day. Two hours, no map needed."),("3:45pm","Printed Matter, 11th Ave at 26th. The artists' bookshop. Half an hour, easily."),("4:30pm","Poster House, W 23rd. The only museum of posters in the country; small, sharp, an hour."),("5:45pm","El Quijote, in the Hotel Chelsea, 23rd and 7th. Reservation pending. Garlic shrimp and a glass of something. Five minutes from the Joyce."),("7:30pm","The Joyce. The Surge: An Ode to Sinéad O'Connor, Sonya Tayeh's company of ten women dancing to Sinéad. Sold-out run."),("9:30pm","Cab home.")],
      food=("Garlic shrimp at El Quijote","The old Spanish room in the Hotel Chelsea, back after the renovation. The pre-theater dinner that feels like the city."),
      swap="If galleries aren't the mood, the High Line from 20th to 30th and a long drink instead."),
 dict(n=3, dow="Sunday", date="27 September", theme="Harlem, a wine bar and a book, then City Island", line="2", color=L["red"], area="Harlem, then City Island",
      intro="The tour is at 11 and Sammy's is at 5:30. In between, the best part of last time: a glass of wine, a book, a Harlem afternoon with nowhere to be.",
      plan=[("10:30am","2/3 to 135th. The tour meets at 135th and Lenox, in front of the Schomburg."),("11:00am","Historic Harlem walking tour. Around two hours."),("1:15pm","Red Rooster, Lenox at 125th. Marcus Samuelsson's place. Light; dinner is in four hours."),("2:30pm","The wine bar. Barawine on Lenox at 120th, or Vinateria on Frederick Douglass at 119th. Books out. Two hours of nothing."),("4:30pm","Car to City Island, about forty minutes on a Sunday. Walk the avenue to the tip."),("5:30pm","Sammy's Fish Box. Lobster, clams, the noise."),("7:30pm","Car home. Early night.")],
      food=("Sammy's Fish Box","City Island seafood in a room that has never once been quiet."),
      swap="If the tour runs long, Red Rooster goes and snacks come to the wine bar. The wine bar is the point."),
 dict(n=4, dow="Monday", date="28 September", theme="Old New York: the Upper West Side", line="1", color=L["red"], area="Upper West Side",
      intro="Symphony Space is at 95th and Broadway, so the day builds north along the west side and ends there. Zabar's and Gray's are done; this is the rest of the neighborhood.",
      plan=[("10:30am","Levain, W 74th, the original basement. The chocolate chip walnut, warm. One, split."),("11:15am","American Museum of Natural History. The dinosaur halls, the Gilder Center, the planetarium."),("1:30pm","Jacob's Pickles, Amsterdam at 84th. Biscuits, fried chicken, the pickle plate. The neighborhood's loud lunch."),("3:00pm","Riverside Park, from 83rd north along the river. The quieter park, the one locals actually use."),("4:30pm","Book Culture, 112th and Broadway. The Columbia bookstore that isn't Columbia's."),("6:00pm","Early bite or a drink near 95th."),("7:00pm","Symphony Space, till 8:30."),("9:00pm","Home.")],
      food=("The Levain cookie, then biscuits at Jacob's Pickles","One is six ounces of cookie. The other is a biscuit the size of a hand. Neither apologizes."),
      swap="If Natural History runs long, Riverside Park goes. Book Culture stays."),
 dict(n=5, dow="Tuesday", date="29 September", theme="Museum Mile, without the Met", line="6", color=L["green"], area="Upper East Side",
      intro="Museum day. The Met is done, so this is the Frick, back in its mansion after the renovation. Plus the two old-school sweets three blocks away.",
      plan=[("10:30am","The Frick, Fifth Ave at 70th. Vermeer, Rembrandt, Bellini, in the rooms they were bought for, plus the upstairs that was never open before. Two hours."),("1:00pm","Lexington Candy Shop, Lex and 83rd. A 1925 luncheonette. Grilled cheese and the egg cream."),("2:15pm","William Greenberg, Madison and 82nd. The black-and-white cookie."),("2:45pm","Cooper Hewitt at 91st, the design museum in the Carnegie mansion. Ninety minutes. Or the Guggenheim at 89th if the building calls."),("4:30pm","The reservoir loop from 90th. 1.6 miles, skyline on all sides."),("6:00pm","Dinner on the west side or home. Nothing booked.")],
      food=("An egg cream and a black-and-white","Lexington Candy Shop for the first, William Greenberg for the second. The two most New York sweets there are."),
      swap="Neue Galerie is closed Tuesdays. If the Frick is too, the Guggenheim takes the morning and the Frick moves to Thursday."),
 dict(n=6, dow="Wednesday", date="30 September", theme="TKTS, the Library, a matinee, K-town", line="B", color=L["orange"], area="Times Square and Midtown",
      intro="Matinee day, tickets bought the New York way: in line at TKTS when the booth opens. Then the most beautiful free room in the city until curtain.",
      plan=[("9:45am","TKTS, the red steps at 47th and Broadway. Matinee sales open at 10; be in line before. Whatever's best on the board at 2pm. Hadestown if it's there."),("11:00am","The New York Public Library, 42nd and Fifth. The Rose Reading Room, the Map Room, the lions. Free. An hour with a book under the ceiling."),("12:15pm","The Halal Guys, 53rd and 6th, the original cart. Chicken and gyro over rice, white sauce. Eat it standing on the corner, or walk it to Bryant Park."),("1:30pm","The theater, whichever one it is."),("2:00pm","The matinee."),("4:45pm","Out. Walk home. Rest."),("7:30pm","Koreatown, 32nd St. Jongro BBQ, galbi and pork belly at the table."),("10:00pm","Walk home.")],
      food=("The halal cart platter, then Korean barbecue","Lunch standing on a corner, dinner grilled at the table. Midtown's two best meals and neither has a host stand."),
      swap="If TKTS has nothing good, the Lincoln Center booth at 62nd is the other one, and the Library moves to after lunch."),
 dict(n=7, dow="Thursday", date="1 October", theme="Books, pierogi, jazz: Murray Hill to the East Village", line="L", color=L["grey"], area="Murray Hill, Union Square, East Village, West Village",
      intro="The east side below 42nd. A new museum, the best bookstore in the city, the old Ukrainian East Village, and the most famous jazz room in the world.",
      plan=[("10:30am","The Morgan Library, Madison at 36th. The Gutenberg Bible, Morgan's study."),("12:15pm","Walk south. Gramercy Park, Irving Place, the Flatiron."),("1:30pm","The Strand, Broadway and 12th. Eighteen miles of books. An hour, at least."),("3:00pm","St. Marks Place, Tompkins Square, the community gardens."),("4:30pm","A drink at Bar Veloce on 2nd Ave, or coffee at Mud on E 9th."),("6:00pm","Veselka, 2nd Ave and 9th. Pierogi, borscht."),("8:00pm","Village Vanguard, 7th Ave South. The 8 o'clock set."),("10:00pm","Home.")],
      food=("Pierogi at Veselka","The Ukrainian diner that's fed the East Village since 1954."),
      swap="If books win, Tompkins goes and the Strand runs till dinner."),
 dict(n=8, dow="Friday", date="2 October", theme="Queens by the 7 train", line="7", color=L["purple"], area="Jackson Heights and Flushing",
      intro="The 7 train is the itinerary. Two stops, two cuisines, one afternoon.",
      plan=[("11:00am","7 train from Times Square to Jackson Heights-Roosevelt Ave."),("11:30am","74th St for South Asian: dosas, samosas, the sweets shops. Roosevelt under the el for Latin: the Arepa Lady, Colombian, Mexican carts. Graze, don't sit."),("1:15pm","Back on the 7 to Flushing-Main St, the end of the line."),("1:45pm","Nan Xiang Xiao Long Bao for the soup dumplings. Then Xi'an Famous Foods for the cumin lamb noodles."),("3:30pm","Flushing Meadows-Corona Park. The Unisphere, the Queens Museum's Panorama of the city."),("5:30pm","7 train back. Or Astoria for Greek, room permitting."),("7:00pm","Home. Early night, train to Beacon in the morning.")],
      food=("Soup dumplings at Nan Xiang, noodles at Xi'an","Flushing is the real Chinatown now. These two are why."),
      swap="If Jackson Heights takes over, Flushing goes. It happens."),
 dict(n=9, dow="Saturday", date="3 October", theme="Hudson Valley: Beacon by train", line="MN", color=L["teal"], area="Beacon, NY",
      intro="The foliage day, done by train. The Hudson Line runs along the river the whole way north. It's the view the cruises sell, with a museum at the end.",
      plan=[("8:45am","Grand Central. Metro-North Hudson Line to Beacon."),("9:00am","Left side going north, the river side. Palisades, the Tappan Zee, Bear Mountain Bridge, Storm King."),("10:30am","Beacon. Dia is ten minutes from the platform."),("10:45am","Dia Beacon. Serra, Bourgeois, Flavin, Agnes Martin, natural light."),("1:15pm","Lunch on Main Street. It's a mile long."),("2:30pm","Galleries, vintage, the falls at the east end. Mount Beacon for a real hike; otherwise not."),("4:40pm","Train south. Right side this time. Gold light on the water."),("6:15pm","Grand Central. Dinner in Midtown or home.")],
      food=("Whatever's best on Main Street","Beacon's a food town now. Decided on the walk."),
      swap="Storm King instead of Dia if outdoor sculpture wins. Needs a car or the Port Authority bus. A swap, not an addition."),
 dict(n=10, dow="Sunday", date="4 October", theme="The old immigrant city: Lower East Side and Chinatown", line="F", color=L["orange"], area="Lower East Side and Chinatown",
      intro="The most New York food day of the trip. Three of the ten live within six blocks of each other. Go hungry.",
      plan=[("10:15am","Russ & Daughters, E Houston, since 1914. The shop, not the cafe. Bagel, nova, scallion cream cheese. Eat it in the park across the street."),("11:30am","Orchard, Ludlow, the tenement blocks."),("12:30pm","The Tenement Museum again, or the galleries on Orchard instead."),("2:00pm","Katz's. Pastrami on rye, mustard, a half-sour. The ticket at the door stays in a pocket. One sandwich, split; it's a pound."),("3:15pm","Yonah Schimmel's, since 1910. A potato knish for later."),("3:45pm","South into Chinatown. Canal, Mott, Doyers."),("4:15pm","Nom Wah Tea Parlor, Doyers St, since 1920. Har gow, siu mai, the original egg roll."),("6:30pm","Home. No dinner required.")],
      food=("Russ & Daughters, Katz's, Nom Wah","Numbers one, two and five on the list, in walking order."),
      swap="Also the right day for Sammy's if the landing weekend ran too full."),
 dict(n=11, dow="Monday", date="5 October", theme="Williamsburg by ferry", line="NYC Ferry", color=L["teal"], area="Williamsburg, Brooklyn",
      intro="The East River ferry from W 39th is a five-minute walk from home and the best way in. The skyline from the water is the point.",
      plan=[("11:00am","Ferry to North Williamsburg, twenty minutes."),("11:30am","Coffee at Devocion on Grand St, or Bakeri on Wythe."),("12:30pm","Domino Park and the waterfront. The old sugar refinery."),("1:30pm","Light lunch. Dinner is the point."),("2:30pm","Bedford Ave and the side streets. Vintage, records, the bookshops. Bar Blondeau on the Wythe roof if the weather holds."),("5:00pm","Maison Premiere, 298 Bedford. The oyster happy hour, then the seafood tower. Absinthe, optionally."),("7:30pm","Walk the Williamsburg Bridge back if it's a good night. Or the ferry.")],
      food=("The seafood tower at Maison Premiere","Oysters, the New Orleans bar, the garden. The Brooklyn night."),
      swap="Peter Luger is a five-minute walk if steak beats oysters. A swap, not both."),
 dict(n=12, dow="Tuesday", date="6 October", theme="Tip to Tip: the whole island on foot", line="A", color=L["blue"], area="Inwood to the Battery",
      intro="The length of Manhattan. Inwood to the Battery, about thirteen miles down Broadway. Long promised. This is the day. Nothing after it.",
      plan=[("8:30am","A train to Inwood-207th, the last stop."),("9:00am","Inwood Hill Park. The northern tip, the last natural forest on the island. Touch the water, then head south."),("10:00am","Washington Heights. Fort Tryon and the Cloisters, a twenty-minute detour uphill."),("11:15am","Malecon, Broadway at 175th. Dominican. Mofongo or the rotisserie chicken."),("12:30pm","Hamilton Heights, Sugar Hill, through Harlem."),("2:00pm","Down Broadway or through the park on the west side."),("3:30pm","Columbus Circle. Halfway. Sit."),("5:30pm","The Village, SoHo, Tribeca."),("6:30pm","The Battery. The southern tip. Look at the Statue. Done."),("7:00pm","Frenchette in Tribeca. Then a car home. Not the subway.")],
      food=("Mofongo at Malecon","Washington Heights is Dominican. Malecon is the Dominican restaurant. It's right on the route."),
      swap="If thirteen miles is too much, the walk starts at the Cloisters instead of Inwood and loses the first three."),
 dict(n=13, dow="Wednesday", date="7 October", theme="SoHo and the Village, then the Golden", line="1", color=L["red"], area="SoHo, West Village, Theater District",
      intro="Operation Mincemeat is at 2 on 45th, so the morning is downtown, starting with the one pastry that has a line at 8am.",
      plan=[("9:00am","Dominique Ansel, Spring St. The Cronut."),("9:45am","SoHo before the crowds. Cast iron on Greene and Mercer."),("10:30am","The West Village. Grove Court, Commerce St, the Cherry Lane block. The prettiest twenty minutes in Manhattan."),("11:30am","Washington Square Park."),("12:00pm","Joe's Pizza, Carmine St, since 1975. Plain slice, folded, at the counter."),("12:20pm","Mamoun's, MacDougal, since 1971. Falafel, hot sauce, eaten walking."),("1:30pm","John Golden Theatre, 252 W 45th."),("2:00pm","Operation Mincemeat. Two hours thirty-five."),("4:45pm","Out. Walk home. Evening open.")],
      food=("The slice at Joe's, the Cronut at Dominique Ansel","One is fifty years old and costs four dollars. The other is twelve years old and needs a pre-order. Both are the city."),
      swap="If the Cronut line is absurd, skip it. Joe's is the one that matters. Tickets for this one are bought ahead, not at TKTS; the morning's downtown."),
 dict(n=14, dow="Thursday", date="8 October", theme="The 9/11 Museum, then Brooklyn: the bridge, DUMBO, the Heights", line="F", color=L["orange"], area="Lower Manhattan, DUMBO, Brooklyn Heights, Downtown Brooklyn",
      intro="The museum first, at opening, while it's quiet. Then straight onto the bridge; the walk is the right thing after. The other Brooklyn on the far side: the coal oven and the cheesecake.",
      plan=[("9:00am","9/11 Memorial and Museum, the first slot of the day. The memorial pools outside, then the museum. Give it two hours; it needs them."),("11:15am","Walk five minutes to City Hall and onto the Brooklyn Bridge. Thirty minutes across, slowly."),("12:00pm","DUMBO. The Manhattan Bridge framed by Washington St, Empire Stores, the waterfront."),("12:30pm","Juliana's, Old Fulton St. Coal-oven pizza, Patsy Grimaldi's own place. There'll be a line; it moves."),("2:00pm","Up into Brooklyn Heights. The Promenade, then Willow, Pierrepont, Montague."),("3:30pm","Junior's, Flatbush and DeKalb, since 1950. The plain cheesecake, in the diner."),("5:00pm","Back over the bridge, or the F home."),("Evening","Beyonce, Homecoming, at home. Screen it, build the food around it. Long overdue.")],
      food=("Coal-oven pizza at Juliana's, cheesecake at Junior's","The Brooklyn half of the pizza argument, and the only cheesecake that counts."),
      swap="Homecoming becomes a Frenchette dinner if Tuesday's attempt didn't land."),
 dict(n=15, dow="Friday", date="9 October", theme="Cooking day: the Greenmarket, then home", line="N", color=L["yellow"], area="Union Square, then home",
      intro="Emmy eve. Cooking at home, together. The Union Square Greenmarket runs Wednesday, Friday and Saturday. Friday is the one.",
      plan=[("9:00am","Union Square Greenmarket. Go early; the good stuff goes by 11. Hudson Valley apples and cider, squash, the last tomatoes, mushrooms, upstate cheese, bread."),("10:30am","One more stop as needed. Eataly on 23rd for pasta and a bottle, or Zabar's for smoked fish and cheese."),("12:00pm","Home. Everything on the counter."),("12:30pm","Cook. Slowly. Music on. A braise, a roast chicken, a squash risotto, an apple tart."),("6:00pm","Dinner at the table. Whatever got made."),("9:30pm","Bed. Tomorrow's the big one.")],
      food=("Whatever the market has","No menu until the market. Whatever's best, and a meal built around it."),
      swap="None. This day is the swap for everything else."),
 dict(n=16, dow="Saturday", date="10 October", theme="The Emmys", line="Car", color=L["yellow"], area="Times Square, the Marriott Marquis",
      intro="Timed backward from the 3:45 car. Everything before it exists to get out the door on time and unhurried.",
      plan=[("8:30am","Up. Real breakfast."),("10:00am","Drybar blowout. One block away."),("11:30am","Light lunch. Nothing that risks the dress."),("12:30pm","Makeup and hair at home, at an easy pace, nobody else in the apartment."),("1:00pm","Lloyd: shower, tux. A separate clock."),("2:30pm","Dress on. Photos in the apartment; there's no quiet minute later."),("3:30pm","By the door: tickets, ID, chargers, flats for later."),("3:45pm","Car."),("4:00pm","The Marriott Marquis. Red carpet, reception, ceremony."),("Late","Walk home. It's ten minutes.")],
      food=("Whatever they serve","And a real breakfast beforehand, because it's a long way till then."),
      swap="Nothing to swap."),
 dict(n=17, dow="Sunday", date="11 October", theme="Departure", line="JFK", color=L["grey"], area="Home, then Terminal 4",
      intro="The last slow one.",
      plan=[("Morning","No alarm. Papers."),("12:00pm","Pack."),("1:30pm","Last lunch, somewhere from this trip worth repeating. Not somewhere new."),("3:30pm","Home. Final pack."),("5:30pm","Car to JFK, Terminal 4. Ninety minutes on a Sunday evening is safe."),("7:00pm","JFK. Business class, the lounge."),("8:55pm","SQ 25. Frankfurt 10:40am Monday.")],
      food=("The one worth a second visit","That's the test of the trip."),
      swap="Nothing, except the car."),
]

SPOTLIGHTS = {
 2: dict(
   headline="Chelsea: art in the old taxi garages, Spain in the Hotel Chelsea, and Sinéad on Eighth Avenue.",
   items=[
    ("The Chelsea galleries","Two hundred galleries, every door free",
     "In the mid-1990s the galleries fled SoHo, priced out by the boutiques that followed them, and took over the garages and warehouses west of Tenth Avenue. Matthew Marks and Paula Cooper went first; Gagosian, Zwirner, Pace and Hauser & Wirth built ground-up temples. It is now the densest concentration of contemporary art on earth, and Saturday afternoon is when it hums.",
     "22nd Street door to door. Zwirner on 19th and 20th. Gagosian's hangar on 24th."),
    ("Printed Matter","Where the book is the art, since 1976",
     "Founded by Sol LeWitt and Lucy Lippard on one radical idea: a book could be the artwork itself, not the catalogue of it. Fifty years on it is the largest nonprofit in the world devoted to artists' books and the engine behind the New York Art Book Fair. Nothing else in the city looks like it.",
     "The zine wall. The cheap table by the door. Anything under ten dollars, which is most of it."),
    ("Poster House","The country's only poster museum",
     "Opened in 2019 on West 23rd, a block from the Hotel Chelsea. Two or three shows at a time: Mucha, Swiss modernism, protest graphics, the golden age of the movie one-sheet. Small enough to see completely, sharp enough to argue about after.",
     "The shop, which is half the point. Whatever is on the ground floor."),
    ("El Quijote","The Spanish room in the Hotel Chelsea. Reservation pending.",
     "A 1930 Spanish restaurant that moved into the Chelsea in 1955 and became the hotel's dining room for the people upstairs: Dylan Thomas, Janis Joplin, Leonard Cohen, Patti Smith and Robert Mapplethorpe when they could afford it. It closed with the hotel in 2018 and reopened in 2022 with the Don Quixote murals restored and the lobster tank back in the window.",
     "The garlic shrimp. The lobster, which was always the thing. A pitcher of sangria before the curtain."),
    ("The Surge, at the Joyce","An ode to Sinéad O'Connor",
     "Sonya Tayeh, Tony-winning choreographer of Moulin Rouge!, built a full-length dance work on Sinéad's music and her own voice from the memoir Rememberings. Ten women, ages 43 to 67, five hundred years of dancing between them, in a field that retires performers at 35. Commissioned by the Joyce and Manchester's Factory International. The run sold out; this is one of its last nights.",
     "Seats close; the Joyce's back row beats most theaters' tenth. A drink at El Quijote first, then eighty minutes of Sinéad."),
   ]),
}

SPOTLIGHTS.update({
 3: dict(headline="Harlem in the morning, a book and a glass of wine in the afternoon, and lobster on an island the Bronx forgot to tell anyone about.",
  items=[
   ("The Historic Harlem tour","Dutch village to the Renaissance, on foot","Two hours from the Schomburg down through Strivers' Row, the Abyssinian Baptist Church and the Apollo, with a guide who knows which stoop Langston Hughes sat on. Harlem was a Dutch farm village, then a white suburb, then, after 1905, the capital of Black America. The blocks still tell it.","Strivers' Row on 138th and 139th, the finest row houses in the city. The Apollo marquee. The plaque outside the Hotel Theresa."),
   ("Red Rooster","Marcus Samuelsson's Harlem, since 2010","Named for a speakeasy that stood a few blocks away, the Rooster brought a two-Michelin-star chef to Lenox Avenue and made the room feel like a block party anyway. Cornbread arrives in a skillet. Obama ate here in his first year.","The fried yardbird if it's a real lunch. The cornbread and a cocktail if it isn't. The Ginny's Supper Club stairs, just to look."),
   ("The wine bar","Barawine or Vinateria, books out","Barawine on Lenox at 120th is French-run, long, and doesn't mind an afternoon that turns into evening. Vinateria on Frederick Douglass is smaller, Italian-leaning, with the better wine list. Both are the kind of room where a book is welcome and the second glass is assumed.","A bottle, not glasses. A plate of something. Two hours minimum."),
   ("City Island","A New England fishing village at the end of the 6 train","A mile and a half long, one avenue wide, with clam shacks, boatyards and Victorian houses, and it has been that way since the 1800s. The rest of the Bronx is a short bridge away and feels like another country. Walk the avenue to Belden Point and look at the water.","The walk to the tip. The nautical museum if it's open. The sunset over the Sound on the way back."),
   ("Sammy's Fish Box","Since 1966, and never once quiet","The lobster place at the end of City Island Avenue, with the neon, the fish tanks and the plates the size of tires. It is loud, it is family, and it is the reason to make the trip. A Sunday here is what a Sunday in the Bronx looks like.","The whole lobster. Fried clams for the table. Whatever's on the sign out front."),
  ]),
 4: dict(headline="The Upper West Side is the New York of the movies: brownstones, the museum, the park from the west, and a cookie the size of a fist.",
  items=[
   ("Levain","The six-ounce cookie, since 1995","Two triathletes opened a basement bakery on West 74th and baked an oversized chocolate chip walnut cookie as training fuel. It became the most famous cookie in America. The original is still the basement, still the line, still warm.","The chocolate chip walnut, split. Dark chocolate peanut butter if there's room. Eat it on the stoop."),
   ("American Museum of Natural History","Dinosaurs, the planetarium, and the new Gilder Center","Founded in 1869, it has the blue whale, the Tyrannosaurus, the Hall of Ocean Life and the Hayden Planetarium's sphere. The Gilder Center, opened in 2023, is the part almost nobody has seen yet: a cave-like building of poured concrete with a butterfly vivarium and the insectarium.","The dinosaur halls on 4. The Gilder Center's insectarium. The whale, because it's the whale."),
   ("Jacob's Pickles","Biscuits and pickles on Amsterdam","Opened in 2011 and immediately the neighborhood's loud lunch: biscuit sandwiches, fried chicken, pickle flights, craft beer on tap. The room is wood and brick and never empty. It is comfort food with a line, and the line is fair.","The pickle sampler. Any biscuit sandwich. The biscuits and gravy if the walk was long."),
   ("Riverside Park","Olmsted's other park, along the river","Four miles of park designed by Frederick Law Olmsted in 1875, terraced down to the Hudson. It has the 79th Street Boat Basin, the Soldiers' and Sailors' Monument, and none of Central Park's crowds. Locals walk here. Tourists don't know it's there.","The promenade at 83rd. The boat basin. The bench with the river and New Jersey going gold."),
   ("Book Culture","The neighborhood bookstore that survived","Since 1997 on 112th Street, a block from Columbia, the shop that outlasted the chains and the internet. Two floors, real staff picks, and a table of new fiction that changes weekly. The kind of place where an hour disappears.","The staff picks table. The basement. One book that wasn't planned."),
  ]),
 5: dict(headline="Museum Mile, done differently: the Frick back in its mansion, an egg cream at a 1925 counter, and the reservoir at golden hour.",
  items=[
   ("The Frick","Vermeer and Rembrandt, in the rooms they were bought for","Henry Clay Frick's 1914 mansion on Fifth Avenue reopened in 2025 after a five-year renovation that opened the family's upstairs rooms to the public for the first time. Three Vermeers, Rembrandt's self-portrait, Bellini's St. Francis, Holbein's Thomas More, hung as a house, not a museum.","The Garden Court with the fountain. Bellini's St. Francis in the Living Hall. The upstairs bedrooms, new since the reopening."),
   ("Lexington Candy Shop","A 1925 luncheonette, unchanged","The last real soda fountain on the Upper East Side, run by the same family since it opened. Chrome stools, a griddle, Coca-Cola made from syrup and seltzer at the counter. The egg cream here is the reference point for every other egg cream.","The egg cream, chocolate. A grilled cheese or a tuna melt. The vintage Coke bottles along the wall."),
   ("William Greenberg","The black-and-white cookie, since 1946","A Madison Avenue bakery that has made the same cookie for eighty years: a soft cake base, half vanilla fondant, half chocolate. Seinfeld made it famous; Greenberg's made it right. The line on Saturday mornings is Upper East Side grandmothers.","The black-and-white, obviously. A brownie for later. The rugelach."),
   ("Cooper Hewitt","The Smithsonian's design museum, in Carnegie's house","Andrew Carnegie's 1902 mansion on 91st Street, now the only museum in the country devoted entirely to design. Typefaces, chairs, wallpaper, the history of everything made. The interactive pen lets visitors save what they liked and look it up later.","The Carnegie library. The garden. The pen; it works."),
   ("The Reservoir","1.6 miles, flat, the skyline on every side","Built in 1862 to supply the city's water, retired in 1993, and now the best running loop in Manhattan. The soft-surface track circles a billion gallons of still water with the Upper West Side towers reflected in it. At golden hour it is the most beautiful place in the park.","The full loop from the 90th Street gate. The bridle path below it if the track's crowded. Sunset from the west side."),
  ]),
 6: dict(headline="Midtown the way New Yorkers do it: a ticket in line, a book under the Library ceiling, lunch from a cart, and a show at two.",
  items=[
   ("TKTS","Half-price tickets, since 1973","The red steps at Duffy Square have sold discounted same-day Broadway tickets since 1973. The board goes up, the line moves, the tickets are real. It is how New Yorkers see theater without planning, and standing in it at ten in the morning is its own small ritual.","Be in line before ten. Take what's best on the board, not what was planned. The red steps after, with a coffee."),
   ("The Rose Main Reading Room","The most beautiful free room in the city","The New York Public Library's main branch opened in 1911; the Rose Reading Room is 78 feet wide, 297 feet long, with a ceiling of painted clouds restored in 2016. Anyone can walk in and sit. The Map Room downstairs is smaller and stranger.","The reading room, an hour with a book. The Map Room. The lions, Patience and Fortitude, on the way out."),
   ("The Halal Guys","The original cart, 53rd and 6th","Three Egyptian immigrants started selling chicken and rice to cab drivers from a cart on this corner in 1990. It became the most famous street food in New York and a global chain, but the cart is still here, on the southeast corner, with the white sauce and the line.","Chicken and gyro combo over rice. White sauce, a little red. Eat it standing, or walk it to Bryant Park."),
   ("The matinee","Whatever the board said","If Hadestown is on the board, it's the one: Anaïs Mitchell's folk-opera retelling of Orpheus and Eurydice, eight Tonys in 2019, still the best-sounding show in the district. If not, the board decides. Two hours in the dark in the middle of a Wednesday is the point.","The best seats TKTS has. No phone. Dinner after, not before."),
   ("Koreatown","32nd Street, three floors of barbecue","One block between Fifth and Broadway, open until 4am, with Korean barbecue stacked above Korean bakeries stacked above karaoke rooms. Jongro BBQ, upstairs, does galbi and pork belly on charcoal at the table and is the place locals argue for.","Galbi and samgyeopsal, grilled at the table. The banchan, all of it. Soju if the matinee was good."),
  ]),
 7: dict(headline="The east side below 42nd: a banker's library, eighteen miles of books, a Ukrainian diner, and the basement where jazz lives.",
  items=[
   ("The Morgan Library","J.P. Morgan's private library, opened to the public in 1924","Charles McKim built Morgan a Renaissance palazzo on 36th Street in 1906 to hold his manuscripts. It has three Gutenberg Bibles, Mozart's handwritten scores, Dickens's manuscripts and Morgan's own study, red-walled and exactly as he left it. Renzo Piano added the glass atrium in 2006.","The East Room, three tiers of books. Morgan's study. Whatever manuscript is on display in the rotunda."),
   ("The Strand","Eighteen miles of books, since 1927","The last survivor of Book Row, the stretch of Fourth Avenue that once held forty-eight bookstores. Three floors and a basement on Broadway at 12th, with the rare book room upstairs and the dollar carts outside. It has never been anything but a bookstore.","The dollar carts on the sidewalk. The rare book room on 3. One book that wasn't planned."),
   ("The East Village","St. Marks, Tompkins Square, the gardens","Once the Lower East Side's northern half, then the center of every counterculture the city had: the Beats, punk at CBGB, the squatters, the Ukrainians who never left. Tompkins Square Park is the neighborhood's living room. The community gardens on the avenues are its secret.","St. Marks Place from Third to Avenue A. Tompkins Square on a weekday. The 6th and B garden."),
   ("Veselka","Pierogi and borscht since 1954","A Ukrainian diner on Second Avenue that has fed the neighborhood around the clock for seventy years. The pierogi are made by hand in the basement. The borscht is the reference. The room is Formica and photographs and has never been renovated on purpose.","Pierogi, boiled, with onions and sour cream. The borscht. The Christmas borscht if it's on."),
   ("The Village Vanguard","The basement, since 1935","Max Gordon opened it as a poetry club in a Greenwich Village cellar; it became the most important jazz room in the world. Coltrane, Bill Evans, Sonny Rollins and a hundred others recorded live albums here. It is still a triangle of a room with 123 seats and no talking.","The 8pm set. A seat along the wall. No phone, no talking, one drink."),
  ]),
 8: dict(headline="One train, two neighborhoods, a dozen countries. The 7 is the most delicious subway line in the world.",
  items=[
   ("Jackson Heights","Six blocks, most of the planet","Under the elevated 7 at Roosevelt Avenue, the most diverse neighborhood on earth: Colombian, Ecuadorian, Mexican, Tibetan, Nepali, Bangladeshi, Indian, all within a ten-minute walk. 74th Street is South Asian. Roosevelt under the tracks is Latin America. Nobody sits; everybody eats.","Momos from a Tibetan counter on 74th. A dosa. The sweets shops. The Arepa Lady's cart under the tracks."),
   ("The Arepa Lady","A Colombian legend under the el","María Piedad Cano sold arepas from a cart under the 7 train for twenty-five years, a former judge from Medellín who became the most famous street vendor in Queens. Her sons now run a storefront on 37th Avenue, but the arepa de queso is the same: griddled corn, butter, cheese.","The arepa de queso. The arepa de choclo, sweeter. A Colombian soda."),
   ("Nan Xiang Xiao Long Bao","The soup dumpling, done properly","Flushing's soup dumpling specialist since 2006, named for the Shanghai town that invented xiao long bao. The dumplings arrive in bamboo steamers, thin-skinned, full of broth. The move: bite, sip, then eat. The line is part of it.","Pork xiao long bao, a basket each. The crab and pork if it's on. Scallion pancake for the table."),
   ("Xi'an Famous Foods","Hand-pulled noodles from a Flushing basement","Jason Wang's father opened a stall in the Golden Shopping Mall basement in 2005, selling the food of Xi'an, the old Silk Road capital: cumin lamb, biang biang noodles, liang pi. It became a chain across the city, but Flushing is where it began and where it's best.","Spicy cumin lamb hand-ripped noodles. Liang pi cold noodles. The lamb burger."),
   ("Flushing Meadows","The World's Fair grounds, and the Panorama","Two World's Fairs, 1939 and 1964, left the Unisphere, the towers, and the Queens Museum. Inside the museum is the Panorama of the City of New York, a scale model of every building in the five boroughs commissioned by Robert Moses in 1964 and still updated. It takes the breath.","The Unisphere up close. The Panorama; find the apartment. The walk along the fountains."),
  ]),
 9: dict(headline="Ninety minutes up the Hudson by train, a museum in a box factory, and a mile of Main Street in a town the city forgot to ruin.",
  items=[
   ("The Hudson Line","The river out the window, the whole way","Metro-North's Hudson Line runs along the water from Spuyten Duyvil north: the Palisades, the Tappan Zee, Croton Point, Bear Mountain Bridge, Storm King, the river widening at Newburgh Bay. In October it is the best foliage view in the state, and it costs a train ticket.","Left side going north, right side coming back. The stretch past Bear Mountain. The morning light."),
   ("Dia Beacon","Minimalism in a Nabisco box factory","Dia opened in 2003 in a 1929 printing plant where Nabisco made its cracker boxes, 300,000 square feet of natural light. Richard Serra's torqued ellipses, Dan Flavin's fluorescent halls, Louise Bourgeois's spiders, Agnes Martin's grids. It is the best museum in the region and it's an hour and a half from Grand Central.","The Serras, walk inside them. The Flavin corridor. The Agnes Martin room, alone."),
   ("Main Street","A mile long, and all of it alive","Beacon was a hat-factory town that died in the 1970s and came back with Dia. Main Street runs a mile from the river to the mountain: galleries, vintage, a bookshop, bakeries, two breweries, and the falls of Fishkill Creek at the east end behind the old factories.","Lunch wherever the walk lands. The east end and the falls. Hudson Beach Glass, the old firehouse."),
   ("Mount Beacon","The optional summit","The hill above town, with the ruins of the 1902 incline railway on the way up and a fire tower at the top. Steep, two hours round trip, and the view is the whole Hudson Highlands. Not a lazy afternoon; a real hike. Only if the mood says so.","The incline railway ruins. The fire tower. Or the bench at the bottom with a coffee."),
   ("Storm King","The swap, if sculpture wins","Five hundred acres of rolling meadow across the river with monumental sculpture set into it: Calder, Serra, Maya Lin's Wavefield, Andy Goldsworthy's stone wall snaking through the trees. Open since 1960. Needs a car or the bus from Port Authority. A day of its own, not an add-on.","Goldsworthy's wall. Maya Lin's field. The Calders on the hill."),
  ]),
 10: dict(headline="The neighborhood every New York family came through. Bagels, pastrami, a knish and dim sum, in walking order, and all of it over a hundred years old.",
  items=[
   ("Russ & Daughters","Appetizing since 1914","Joel Russ sold herring from a pushcart, opened a shop on Houston Street in 1914 and, in 1935, made his three daughters partners, the first American business to put 'and Daughters' on the sign. Four generations on, it is the definitive smoked fish counter in the city. Take a number.","Bagel, Gaspe nova, scallion cream cheese. A piece of sable. The chocolate babka for later."),
   ("The Tenement Museum","Real apartments, real families","97 Orchard Street housed 7,000 immigrants between 1863 and 1935; the museum found the building sealed in 1988 and restored the apartments as they were left. Guided tours only, one family per tour, and the story of the neighborhood told through their rooms. One of the best museums in New York.","Whichever tour has a slot. Orchard Street after, the same blocks."),
   ("Katz's Delicatessen","Since 1888, and the pastrami is why","The last of the great Lower East Side delis, in the same spot since 1888. Take the ticket at the door, order at the counter, watch the cutter hand over a slice while he carves. The pastrami is smoked for weeks and sliced by hand. The room is where Harry met Sally.","Pastrami on rye, mustard. A half-sour from the plate. Dr. Brown's cel-ray if the nerve is there."),
   ("Yonah Schimmel's","The knish, since 1910","A Romanian rabbi's pushcart became a Houston Street storefront in 1910, and it has made potato knishes in the same basement oven ever since. The room has not changed. The knish is a pound of mashed potato in a thin crust and it is the neighborhood in one bite.","Potato knish, plain. Kasha if adventurous. Eat it later; it travels."),
   ("Nom Wah Tea Parlor","Dim sum on Doyers, since 1920","The oldest dim sum house in the city, on the crooked block of Doyers Street once called the Bloody Angle. Red vinyl booths, tiled floor, the original egg roll that isn't like any other. Bought by the owner's nephew in 2010 and kept exactly as it was.","Har gow, siu mai, the original egg roll. Turnip cake. The house tea."),
  ]),
 11: dict(headline="Take the ferry. Brooklyn's waterfront was sugar and shipping; now it's coffee, oysters and the skyline you came for.",
  items=[
   ("The East River ferry","Twenty minutes, three dollars, the whole skyline","NYC Ferry launched in 2017 and made the water a commute again. From West 39th around the Battery and up the East River to North Williamsburg, with Midtown, the bridges and Lower Manhattan going past the window. It is the best way into Brooklyn and it costs less than a coffee.","The top deck, outside. The stretch under the bridges. A seat on the Manhattan side."),
   ("Devoción","Colombian coffee under a skylight","A Bogotá-born roaster whose Grand Street cafe is a former warehouse filled with plants and light. The beans are flown in fresh from Colombia weekly, which nobody else does. It is the best cup in Williamsburg and the room to drink it in.","A pour-over, single origin. The pastry case. The bench under the skylight."),
   ("Domino Park","The sugar refinery, reborn","The Domino Sugar Refinery closed in 2004 after 150 years; the park opened on its waterfront in 2018, with the old gantry cranes, syrup tanks and the brick refinery kept as sculpture. A quarter mile of river with the Williamsburg Bridge overhead and Manhattan across the water.","The elevated walkway. The old cranes. The view back at the Empire State from the water."),
   ("The Wythe rooftop","Bar Blondeau, the skyline as a drink","The Wythe Hotel, a converted 1901 cooperage, opened in 2012 and set the tone for the neighborhood. Its sixth-floor bar, Bar Blondeau, has floor-to-ceiling windows and the definitive view of Manhattan from Brooklyn. Weather permitting, the terrace.","A drink at golden hour. The terrace if it's open. Oysters here or save them."),
   ("Maison Premiere","New Orleans in Brooklyn, oysters and absinthe","Opened in 2011 on Bedford Avenue as an oyster and absinthe bar modeled on the French Quarter. A horseshoe marble bar, thirty kinds of oysters, an absinthe fountain and a garden out back. James Beard nominated, and the best seafood tower in the borough.","The happy hour oysters, then the tower. An absinthe drip, once. The garden if the night is warm."),
  ]),
 12: dict(headline="Thirteen miles, top to bottom: a forest, a monastery, mofongo, the whole spine of Broadway, and the Statue at the end of it.",
  items=[
   ("Inwood Hill Park","The last forest on the island","The northern tip of Manhattan, and the only place on it that was never cleared: old-growth forest, caves the Lenape used, salt marsh where the Harlem and Hudson rivers meet. A boulder marks where the island was supposedly bought in 1626. The city is invisible from here.","The caves. The marsh at the tip. Shorakkopoch Rock and the plaque."),
   ("The Cloisters","Medieval Europe on a hill over the Hudson","The Met's medieval branch, built in 1938 from pieces of five French monasteries, shipped stone by stone and reassembled in Fort Tryon Park with Rockefeller's money. The Unicorn Tapestries are here. So are the gardens, planted from medieval texts. The Palisades across the river were bought to keep the view.","The Unicorn Tapestries. The Cuxa Cloister garden. The view from the ramparts."),
   ("Malecon","Dominican Washington Heights, on a plate","Washington Heights is the largest Dominican community outside the Dominican Republic, and Malecon on Broadway at 175th is its restaurant: rotisserie chicken turning in the window since 1990, mofongo, oxtail, rice and beans in portions built for people who have been walking.","Mofongo with the garlic. The rotisserie chicken. A morir soñando."),
   ("Broadway, the long way","From the Heights to the Battery","Broadway is the oldest road on the island, the Lenape trail the Dutch paved, and it runs the full length: Washington Heights, Harlem, the Upper West Side, Columbus Circle, Times Square, the Flatiron, SoHo, City Hall, the Battery. Every neighborhood changes underfoot.","Columbus Circle, halfway, sit. Cut west to the Hudson Greenway through Midtown. Back to Broadway at Union Square."),
   ("The Battery","The southern tip, and the Statue","The park at the bottom of the island, where the Dutch built their fort in 1626 and where the ferries to Liberty and Ellis Island still leave. Castle Clinton, the SeaGlass Carousel, and the promenade with the Statue of Liberty out in the harbor. After thirteen miles, the water.","The promenade at the tip. The Statue, from a bench. Frenchette in Tribeca after, then a car."),
  ]),
 13: dict(headline="A pastry with a line at eight in the morning, the prettiest streets in Manhattan, a four-dollar slice, and a wartime spy caper at two.",
  items=[
   ("Dominique Ansel","The Cronut, since 2013","A French pastry chef in a small SoHo bakery laminated croissant dough, fried it like a doughnut, filled it with cream and named it. Within a week there were lines at 6am and a black market. Thirteen years later the flavor changes monthly and the line is shorter, but the pre-order is still smart.","The Cronut, this month's flavor. The DKA, the pastry insiders order. A frozen s'more if it's warm."),
   ("SoHo's cast iron","The biggest cast-iron district in the world","Twenty-six blocks of 1870s factories with cast-iron facades, bolted together from catalogue parts and painted to look like stone. Abandoned by industry, taken by artists in the 1960s, and now the most photographed streetscape downtown. Before ten, it's empty.","Greene Street from Canal to Houston. The Haughwout Building on Broome. Mercer Street's cobbles."),
   ("The West Village","Where the grid breaks","Below 14th, the streets stop being numbers and start being names, and they bend. Grove Court's hidden row of 1850s houses, Commerce Street's curve, the Cherry Lane Theatre, Bank Street's brownstones. It is the neighborhood every film set in New York tries to fake.","Grove Court through the gate. Commerce Street's bend. Cherry Lane, the oldest off-Broadway theater."),
   ("Joe's Pizza","The plain slice, since 1975","Joe Pozzuoli, from Naples, opened on the corner of Bleecker and Carmine and never changed the recipe. Thin, foldable, a little charred, four dollars and eaten standing. It is the slice every other slice in the city is measured against. Spider-Man worked here in the movies.","The plain cheese slice, folded. A second one. Nothing on it."),
   ("Mamoun's","Falafel on MacDougal, since 1971","The oldest falafel shop in the city and the first in Greenwich Village, a counter on MacDougal Street that has fed NYU students, cabbies and Bob Dylan for fifty years. Three dollars, a pita, the hot sauce that made it famous. Eaten on the sidewalk, always.","The falafel sandwich. The hot sauce, carefully. A baklava for the walk to the train."),
   ("Operation Mincemeat","A true wartime caper, sung","In 1943 British intelligence floated a corpse with fake invasion plans off the coast of Spain and fooled Hitler. Four comedians turned it into a musical in a room above a pub in London; it won the Olivier for Best Musical and moved to Broadway in 2025. Five actors play forty parts. It is funnier than it has any right to be.","Seats close; it's a small cast in a small house. The eleven o'clock number. Stay for the bows."),
  ]),
 14: dict(headline="The hardest morning of the trip, then the walk that makes it right: the bridge, the waterfront, coal-oven pizza and the cheesecake.",
  items=[
   ("The 9/11 Memorial and Museum","The pools, then the museum below","Michael Arad's two reflecting pools sit in the footprints of the towers, with the names cut into bronze around the edges and water falling into the void. The museum below, opened in 2014, holds the slurry wall, the last column, the Survivors' Stairs and the stories. It takes two hours and it earns them.","The pools first, outside. The Memorial Hall. The Survivors' Stairs. Then the bridge."),
   ("The Brooklyn Bridge","1883, and still the walk","Fourteen years to build, twenty-seven workers dead, designed by John Roebling and finished by his son and his daughter-in-law Emily after both men were injured. The first steel-wire suspension bridge in the world. The walkway above the traffic, with the Gothic towers and the harbor on both sides, is the best free half-hour in the city.","Walk it from the Manhattan side. Stop at the first tower and look back. Morning light."),
   ("DUMBO","Down Under the Manhattan Bridge Overpass","Warehouses, cobbles and the shot of the Manhattan Bridge framed between the buildings on Washington Street that everyone takes and should. Brooklyn Bridge Park runs along the waterfront below with Jane's Carousel in its glass box and the skyline across the river.","Washington Street at Water Street, the photo. Empire Stores. The waterfront to Pier 1."),
   ("Juliana's","Patsy Grimaldi's own place","Patsy Grimaldi learned from Patsy Lancieri, sold his name in 1998, retired, hated what happened to it, and opened Juliana's next door in 2012 with the coal oven and his mother's name. Thin, blistered, coal-fired, the crust that Brooklyn pizza is supposed to mean.","The classic Margherita. The No. 1, with the sausage. The line moves; join it."),
   ("The Promenade","Brooklyn Heights, and the view","The first historic district in New York, brownstones and Federal houses from the 1820s on, with the Promenade cantilevered over the expressway since 1950. From it: the harbor, the bridge, Lower Manhattan, the Statue. Willow, Pierrepont and Montague Streets behind it are the city's best walk of front doors.","The Promenade end to end. Willow Street. Montague for a coffee."),
   ("Junior's","The cheesecake, since 1950","Harry Rosen's diner at Flatbush and DeKalb opened in 1950 and its cheesecake, dense, plain, on a sponge base, became the one the city means when it says the word. The room is orange booths, a long counter and a display case of the cakes. Sit down; don't take it to go.","Plain cheesecake, a slice. The strawberry if the plain seems too pure. A coffee, in the booth."),
  ]),
 15: dict(headline="Emmy eve. The market at nine, the kitchen by noon, and the one dinner of the trip that gets made, not booked.",
  items=[
   ("Union Square Greenmarket","The city's market, since 1976","It started with twelve farmers in a parking lot and became the largest and best-known farmers market in the country: 140 regional producers on Mondays, Wednesdays, Fridays and Saturdays. In October it is apples, cider, squash, the last tomatoes, mushrooms, upstate cheese and bread. Chefs shop here at dawn.","The apple stands; ask for the odd varieties. The mushroom man. Bread from the bakery stalls. Cider, warm if it's cold."),
   ("Eataly","The Italian market on 23rd, since 2010","Fifty thousand square feet of Italian groceries under the Flatiron: fresh pasta made in the window, a cheese counter, the olive oil wall, a butcher, a fishmonger and a wine shop. The second stop if the market didn't cover it.","Fresh pasta from the counter. A good bottle. Parmigiano, a wedge, for the table."),
   ("The kitchen","Slowly, all afternoon","Whatever the market gave: a braise, a roast chicken, a squash risotto, an apple tart with Hudson Valley fruit. Music on, wine open, no clock. The one meal of the trip that gets made at home, together, the night before the biggest day.","The long recipe, not the fast one. Dessert from the market apples. Bed by half nine."),
  ]),
 16: dict(headline="The last full day, timed to the minute, and the night the whole trip has been pointed at.",
  items=[
   ("Drybar","The blowout, a block away","The chain that made the blowout a category, with a shop a block from the apartment. Forty-five minutes, a menu of styles with cocktail names, and hair that lasts until the car home. Booked early so the afternoon has slack.","The 10 or 10:30 slot. Whichever style survives a red carpet. Photos before the car."),
   ("The New York Emmys","The 69th annual, at the Marquis","The National Academy's New York chapter honors the year's best local television, news and documentary work, and the ceremony is the industry's night out: black tie, red carpet, the ballroom. This year it is the reason the trip ends when it does.","The red carpet, slowly. The ballroom before it fills. The walk home after, ten minutes, in the air."),
   ("The Marriott Marquis","Times Square, 45th floor of it","The 1985 hotel in the middle of Times Square, with the atrium, the glass elevators and the ballroom that hosts half the awards nights in the city. Ten minutes on foot from the apartment, which is the whole point of living where the apartment is.","The atrium elevators, once. The view from the ballroom floor. Times Square after midnight, quieter than expected."),
  ]),
})

NEIGHBORHOODS = [
 ("West Village","The prettiest streets in the city: Grove Court, Commerce, Bank. Coffee, a bookstore, a slice at Joe's, and get lost on purpose.","1 to Christopher St"),
 ("Lower East Side","Russ & Daughters, Katz's, the Tenement Museum, then the galleries on Orchard. The whole immigrant story in six blocks.","F to 2nd Ave"),
 ("Harlem","Lenox and 125th, Strivers' Row, the Apollo, Sylvia's, Minton's at night. The most important neighborhood in Black America.","2/3 to 125th"),
 ("Williamsburg","Bedford Ave, Domino Park, the Wythe roof, oysters at Maison Premiere. Take the ferry; the skyline is the point.","Ferry from W 39th"),
 ("Brooklyn Heights and DUMBO","Walk the bridge, the Promenade for the skyline, the brownstone streets behind it, Juliana's for pizza.","A/C to High St"),
 ("East Village","St. Marks, Tompkins Square, the Strand, Veselka, Veniero's. Still a little scrappy. Best after dark.","6 to Astor Pl"),
 ("Upper West Side","Zabar's, Levain, the Natural History museum, Central Park from the west. The New York of Nora Ephron films.","1 to 79th"),
 ("Jackson Heights","Six blocks under the el with Colombian, Tibetan, Indian, Mexican, Bangladeshi. The most diverse square mile on earth, and it tastes like it.","7 to 74th St"),
 ("Astoria","Greek tavernas, the Noguchi Museum, the Museum of the Moving Image, the beer garden at Bohemian Hall. Queens at its most livable.","N/W to Astoria Blvd"),
 ("Red Hook","The waterfront with the Statue of Liberty right there, Sunny's bar, Steve's key lime pie, the old warehouses. No subway, which is why it's still Red Hook.","Ferry to Red Hook"),
]

FOODS = [
 ("Bagel with lox and schmear","Russ & Daughters, E Houston"),
 ("Pastrami on rye","Katz's Delicatessen, E Houston"),
 ("The plain slice","Joe's Pizza, Carmine St"),
 ("Coal-oven pie","Juliana's, DUMBO, or Lucali, Carroll Gardens"),
 ("Dim sum","Nom Wah Tea Parlor, Doyers St"),
 ("Soup dumplings","Nan Xiang Xiao Long Bao, Flushing"),
 ("Halal cart chicken over rice","The Halal Guys, 53rd and 6th"),
 ("Chicken and waffles","Sylvia's, Harlem"),
 ("The egg cream","Lexington Candy Shop, Lex and 83rd"),
 ("Black-and-white cookie","William Greenberg, Madison Ave"),
 ("Cheesecake","Junior's, Flatbush Ave"),
 ("The Cronut","Dominique Ansel, Spring St"),
 ("The six-ounce cookie","Levain, W 74th"),
 ("Hot dog and papaya juice","Gray's Papaya, 72nd and Broadway"),
 ("Bacon, egg and cheese on a roll","Any bodega, any morning"),
 ("Chopped cheese","Had it in Hell's Kitchen. The bodega version travels."),
 ("Korean barbecue","Jongro BBQ, 32nd St"),
 ("Hand-pulled cumin lamb noodles","Xi'an Famous Foods, Flushing and everywhere"),
 ("Mofongo","Malecon, Washington Heights"),
 ("Fresh mozzarella and a cannoli","Arthur Avenue, the Bronx"),
 ("Pierogi and borscht","Veselka, 2nd Ave"),
 ("Falafel","Mamoun's, MacDougal St"),
 ("The knish","Yonah Schimmel's, E Houston"),
 ("Oysters","Maison Premiere, Williamsburg, or the Grand Central Oyster Bar"),
 ("Porterhouse for two","Peter Luger, Williamsburg. Once."),
]

MUSEUMS = [
 ("The Met","Fifth Ave at 82nd. The one that has everything. Closed Wednesdays."),
 ("MoMA","W 53rd. The modern collection; floors 4 and 5."),
 ("The Whitney","Gansevoort St. American art, the High Line at its feet. Closed Tuesdays."),
 ("The Guggenheim","Fifth Ave at 89th. The building is the exhibit."),
 ("American Museum of Natural History","Central Park West at 79th. Dinosaurs, the planetarium, the Gilder Center."),
 ("The Frick","Fifth Ave at 70th. Vermeer and Rembrandt in a Gilded Age mansion. On the itinerary, Tuesday the 29th."),
 ("Neue Galerie","Fifth Ave at 86th. Klimt, Schiele, and Cafe Sabarsky downstairs. Closed Tuesday and Wednesday."),
 ("The Morgan Library","Madison at 36th. J.P. Morgan's private library, the Gutenberg Bible."),
 ("The Tenement Museum","Orchard St. Guided tours through real preserved apartments. Book ahead."),
 ("Brooklyn Museum","Eastern Parkway. Egyptian collection, the Dinner Party, First Saturdays."),
 ("The Cloisters","Fort Tryon Park. Medieval Europe on a hill over the Hudson. The Unicorn Tapestries."),
 ("The New Museum","The Bowery. Contemporary art in the expanded building."),
 ("The Studio Museum in Harlem","W 125th. Artists of African descent, in its new home."),
 ("Museum of the City of New York","Fifth Ave at 103rd. The city explaining itself."),
 ("Cooper Hewitt","Fifth Ave at 91st. The Smithsonian's design museum, in the Carnegie mansion."),
 ("MoMA PS1","Long Island City. The experimental wing, in an old school."),
 ("The Noguchi Museum","Long Island City. The sculptor's own studio and garden."),
 ("9/11 Memorial and Museum","Lower Manhattan. On the itinerary, Thursday the 8th, first thing."),
 ("Queens Museum","Flushing Meadows. The Panorama: every building in the city, in miniature."),
 ("Dia Beacon","Beacon, NY. Ninety minutes up the Hudson. Already on the itinerary."),
]

RITUALS = [
 ("Ride the Staten Island Ferry at sunset","Free, twenty-five minutes, past the Statue. Stand on the back deck coming home."),
 ("Order a bagel correctly","Everything, scallion cream cheese, nova. Say it fast. Don't ask for it toasted."),
 ("Do the Greenmarket on a Saturday","Union Square. Apples, cider, the bread stalls. This is how New Yorkers shop."),
 ("Sit through a set at the Vanguard","The basement on 7th Ave South. No talking, no phones. Coltrane recorded here."),
 ("Walk a bridge","Brooklyn for the postcard, Williamsburg for the view of it, Manhattan Bridge for the one nobody does."),
 ("Watch a movie at Film Forum","W Houston. Revivals, documentaries, the popcorn. The most New York cinema there is."),
 ("Spend an hour at the Strand","Eighteen miles of books. Leave with one that wasn't on the list."),
 ("Eat standing up","A slice, a cart, a dog. Nowhere to sit is the point."),
 ("Take the ferry instead of the subway","East River, Astoria, Rockaway. Three dollars and the skyline."),
 ("Get lost in the West Village on purpose","The grid breaks. Follow the crooked streets. Come out somewhere unexpected."),
]

BOOKINGS = [
 ("Harlem walking tour","Sun 27 Sep, 11am","Booked. Confirm the end time."),
 ("Dia Beacon","Sat 3 Oct","Timed tickets online. Saturdays sell out."),
 ("Metro-North to Beacon","Sat 3 Oct","Buy in the TrainTime app the night before."),
 ("Village Vanguard","Thu 1 Oct, 8pm","Reserve online. Sells out."),
 ("9/11 Memorial and Museum","Thu 8 Oct, 9am","Book the first slot."),
 ("Operation Mincemeat","Wed 7 Oct, 2pm","Buy ahead. John Golden Theatre."),
 ("TKTS","Wed 30 Sep, 10am","Nothing to book. Be in line by 9:45."),
 ("Maison Premiere","Mon 5 Oct, 5pm","Reserve. Confirm the oyster hour."),
 ("Jongro BBQ","Wed 30 Sep, 7:30pm","Reserve."),
 ("El Quijote","Sat 26 Sep, 5:45pm","Call. Nothing indoor showing online; they often have it by phone. Opens 5pm."),
 ("The Frick","Tue 29 Sep, 10:30am","Confirm Tuesday hours, then timed ticket."),
 ("The Morgan Library","Thu 1 Oct, 10:30am","Timed ticket."),
 ("Cooper Hewitt","Tue 29 Sep, 2:45pm","Timed ticket."),
 ("Poster House","Sat 26 Sep, 4:30pm","Ticket at the door is fine."),
 ("Tenement Museum","Sun 4 Oct, 12:30pm","Only if going again. Guided tours only."),
 ("Frenchette","Tue 6 Oct, 7pm","Try. It's hard."),
 ("Dominique Ansel","Wed 7 Oct","Pre-order the Cronut online."),
 ("Drybar","Sat 10 Oct, 10am","Confirm booked."),
 ("The dress","By Fri 9 Oct","Rent the Runway or hers. Decide."),
 ("SQ 25 check-in","Sun 11 Oct, morning","Confirmation number needed."),
 ("Car to JFK","Sun 11 Oct, 5:30pm","Book."),
]

DONE_FOODS = {"Pastrami on rye","The plain slice","Soup dumplings","Hot dog and papaya juice","Bacon, egg and cheese on a roll","Chopped cheese","The knish"}
DONE_MUSEUMS = {"The Met","MoMA","The Whitney","The Tenement Museum"}
DONE_RITUALS = {"Walk a bridge","Eat standing up","Take the ferry instead of the subway","Get lost in the West Village on purpose"}
CHECK = '<span class="had">&#10003;</span>'

def e(s): return html.escape(s)

def bullet(line, color, size=1.0):
    txt = e(line)
    cls = "bullet" + (" bullet-wide" if len(line) > 2 else "")
    return f'<span class="{cls}" style="background:{color};font-size:{size}em">{txt}</span>'

pages = []

# ---------- Cover ----------
pages.append(f'''
<section class="page cover">
  <div class="cover-sign">
    <div class="cover-kicker">Sarah in New York</div>
    <h1>Part<br>Seven</h1>
    <div class="cover-dates">25 September to 11 October 2026</div>
  </div>
  <div class="cover-right">
    <div class="cover-lines">
      {"".join(bullet(l,c,1.0) for l,c in [("1",L["red"]),("A",L["blue"]),("6",L["green"]),("B",L["orange"]),("7",L["purple"]),("N",L["yellow"]),("L",L["grey"])])}
    </div>
    <p class="cover-note">Seventeen days. One neighborhood a day. Twenty-five foods, twenty museums, ten neighborhoods to choose from. A plan to be marked up together.</p>
    <p class="cover-credit">Lloyd, for Sarah</p>
  </div>
</section>''')

# ---------- How to read ----------
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("i",L["grey"])}<span>How to read this</span></div>
  <div class="two-col">
    <div>
      <h2>The idea</h2>
      <p>Every day is one part of the city, done properly, with the train that gets there on the page. The fixed points are real: the flights, the Joyce, Symphony Space, Sammy's, the two Wednesday matinees, the Emmys. Everything else is designed around them and can move.</p>
      <p>The foods New York is actually known for are placed on the day the plan is already in their neighborhood, so nothing is a detour.</p>
      <h2>The menus at the back</h2>
      <p>The appendices are the menu. Ten neighborhoods worth an afternoon, twenty-five foods to have as a New Yorker, twenty museums, ten things that make a local. Anything circled that isn't already on a day gets a day.</p>
    </div>
    <div>
      <h2>What each day page shows</h2>
      <ul class="legend">
        <li><b>The bullet</b> is the train, ferry or car that gets there.</li>
        <li><b>The plan</b> is hour by hour. Times are starts, not deadlines.</li>
        <li><b>The food</b> is what that day is for, if only one thing happens.</li>
        <li><b>The swap</b> is what changes if the day runs long, or short, or the mood does.</li>
      </ul>
      <h2>Two honest notes</h2>
      <p>Sunday the 27th is a full second day; the wine bar is the part that gives. Tuesday the 6th is thirteen miles; the Cloisters is the shorter start.</p>
    </div>
  </div>
</section>''')


# ---------- Opener: the trip in one look ----------
OPENER_TILES = [
 ("Harlem","Sunday, a tour and a wine bar"),
 ("The Frick","Tuesday, Vermeer in the mansion"),
 ("The Hudson","Saturday, foliage by train to Beacon"),
 ("Katz's","Sunday, pastrami on the Lower East Side"),
 ("The Vanguard","Thursday, the eight o'clock set"),
 ("Flushing","Friday, soup dumplings at the end of the 7"),
 ("The Brooklyn Bridge","Thursday, after the museum"),
 ("The Greenmarket","Friday, then cooking at home"),
 ("The Emmys","Saturday, the last full day"),
]
STATS = [("17","days"),("12","neighborhoods"),("25","foods"),("20","museums"),("2","matinees"),("1","sold-out dance premiere"),("1","jazz set at the Vanguard"),("13","miles, tip to tip"),("1","Emmy night")]

def tile(i, name, cap):
    import os, base64, mimetypes
    src = None
    for ext in ("jpg","jpeg","png","webp"):
        p = f"images/opener/{i+1}.{ext}"
        if os.path.exists(p):
            mime = mimetypes.guess_type(p)[0] or "image/jpeg"
            src = f"data:{mime};base64,{base64.b64encode(open(p,'rb').read()).decode()}"
            break
    plates = [L["red"],L["blue"],L["green"],L["orange"],L["purple"],L["yellow"],L["teal"],L["grey"],L["brown"]]
    bg = f"background-image:url({src})" if src else f"background:{plates[i%len(plates)]}"
    return f'<div class="op-tile" style="{bg}"><div class="op-cap"><b>{e(name)}</b>{e(cap)}</div></div>'

tiles = "".join(tile(i,n,c) for i,(n,c) in enumerate(OPENER_TILES))
stats = "".join(f'<div class="op-stat"><span class="op-num">{e(n)}</span><span class="op-lab">{e(l)}</span></div>' for n,l in STATS)
pages.append(f'''
<section class="page opener">
  <div class="op-left">
    <div class="op-kicker">Sarah in New York, Part Seven</div>
    <h2 class="op-title">Seventeen days,<br>one look</h2>
    <div class="op-stats">{stats}</div>
  </div>
  <div class="op-grid">{tiles}</div>
</section>''')

# ---------- At a glance ----------
cells = ""
for d in DAYS:
    cells += f'''<div class="cal-cell"><div class="cal-top">{bullet(d["line"],d["color"],0.8)}<span class="cal-date">{e(d["dow"][:3])} {e(d["date"].split()[0])}</span></div><div class="cal-theme">{e(d["theme"])}</div></div>'''
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("17",L["yellow"])}<span>The trip at a glance</span></div>
  <div class="cal">{cells}</div>
</section>''')

# ---------- Day pages ----------
for d in DAYS:
    rows = "".join(f'<div class="t-row"><div class="t-time">{e(t)}</div><div class="t-what">{e(w)}</div></div>' for t,w in d["plan"])
    if d["n"] in SPOTLIGHTS:
        sp = SPOTLIGHTS[d["n"]]
        plates = [L["blue"],L["orange"],L["green"],L["red"],L["purple"],L["yellow"],L["teal"]]
        def plate(i):
            import os, base64, mimetypes
            for ext in ("jpg","jpeg","png","webp"):
                p = f"images/day{d['n']}/{i+1}.{ext}"
                if os.path.exists(p):
                    mime = mimetypes.guess_type(p)[0] or "image/jpeg"
                    b64 = base64.b64encode(open(p,"rb").read()).decode()
                    return f'<div class="sp-photo" style="background-image:url(data:{mime};base64,{b64})"><span>{i+1}</span></div>'
            return f'<div class="sp-plate" style="background:{plates[i%len(plates)]}"><span>{i+1}</span></div>'
        blocks = "".join(f'''<div class="sp-item">{plate(i)}<div class="sp-name">{e(nm)}</div><div class="sp-sub">{e(sub)}</div><p class="sp-body">{e(body)}</p><div class="sp-try"><span>Try</span>{e(tr)}</div></div>''' for i,(nm,sub,body,tr) in enumerate(sp["items"]))
        spot = f'''
<section class="page spot">
  <div class="sign-strip">{bullet(d["line"],d["color"])}<span>Day {d["n"]}, up close</span><span class="strip-sub">{e(d["dow"])} {e(d["date"])}</span></div>
  <div class="sp-head">{e(sp["headline"])}</div>
  <div class="sp-grid sp-n{len(sp["items"])}" style="grid-template-columns: repeat({len(sp["items"])}, 1fr)">{blocks}</div>
</section>'''
    else:
        spot = ""
    pages.append(f'''
<section class="page day">
  <div class="sign" style="--line:{d["color"]}">
    <div class="sign-top">{bullet(d["line"],d["color"],1.6)}<div class="sign-day">Day {d["n"]}</div></div>
    <div class="sign-date">{e(d["dow"])}<br>{e(d["date"])}</div>
    <h2 class="sign-theme">{e(d["theme"])}</h2>
    <div class="sign-area">{e(d["area"])}</div>
    <div class="sign-food"><div class="sign-label">The food</div><div class="sign-food-name">{e(d["food"][0])}</div><div class="sign-food-why">{e(d["food"][1])}</div></div>
  </div>
  <div class="body">
    <p class="intro">{e(d["intro"])}</p>
    <div class="timeline">{rows}</div>
    <div class="swap"><span class="swap-label">The swap</span> {e(d["swap"])}</div>
  </div>
</section>''')
    if spot: pages.append(spot)

# ---------- Divider ----------
pages.append(f'''
<section class="page divider">
  <div class="cover-sign" style="width:100%">
    <div class="cover-kicker">Part two</div>
    <h1 style="font-size:5.2em">The menus</h1>
    <div class="cover-dates">Ten neighborhoods. Twenty-five foods. Twenty museums. Ten rituals. Anything circled gets a day.</div>
  </div>
</section>''')

# ---------- Neighborhoods ----------
items = "".join(f'<div class="n-item"><div class="n-name">{e(n)}</div><div class="n-desc">{e(dsc)}</div><div class="n-train">{e(tr)}</div></div>' for n,dsc,tr in NEIGHBORHOODS)
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("10",L["blue"])}<span>Neighborhoods worth an afternoon</span><span class="strip-sub">Three or four hours each. On the itinerary only if circled.</span></div>
  <div class="grid-5">{items}</div>
</section>''')

# ---------- Foods (two pages) ----------
def food_page(chunk, start, label):
    rows = "".join(f'<div class="f-row{" done" if n in DONE_FOODS else ""}"><div class="f-num">{i}</div><div><div class="f-name">{e(n)}{CHECK if n in DONE_FOODS else ""}</div><div class="f-where">{e(w)}</div></div></div>' for i,(n,w) in enumerate(chunk, start))
    return f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("25",L["red"])}<span>Foods to have as a New Yorker</span><span class="strip-sub">{label}</span></div>
  <div class="grid-3">{rows}</div>
</section>'''
pages.append(food_page(FOODS[:13], 1, "One to thirteen. A check means already had."))
pages.append(food_page(FOODS[13:], 14, "Fourteen to twenty-five. A check means already had."))

# ---------- Museums ----------
rows = "".join(f'<div class="m-row"><div class="m-name">{e(n)}{CHECK if n in DONE_MUSEUMS else ""}</div><div class="m-desc">{e(dsc)}</div></div>' for n,dsc in MUSEUMS)
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("20",L["green"])}<span>Museums</span><span class="strip-sub">A check means already visited. The Frick, the Morgan, Cooper Hewitt, Natural History, 9/11 and Dia are on days. The rest are open.</span></div>
  <div class="grid-4">{rows}</div>
</section>''')

# ---------- Rituals ----------
rows = "".join(f'<div class="r-row{" done" if n in DONE_RITUALS else ""}"><div class="r-name">{e(n)}{CHECK if n in DONE_RITUALS else ""}</div><div class="r-desc">{e(dsc)}</div></div>' for n,dsc in RITUALS)
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("10",L["purple"])}<span>Things that make you a New Yorker</span><span class="strip-sub">None of them cost more than a subway fare. A check means done.</span></div>
  <div class="grid-5">{rows}</div>
</section>''')

# ---------- Sarah's picks ----------
def boxes(names):
    done = DONE_FOODS | DONE_RITUALS | DONE_MUSEUMS
    return "".join(f'<div class="pick"><span class="box{" ticked" if n in done else ""}">{"&#10003;" if n in done else ""}</span>{e(n)}</div>' for n in names)
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("S",L["yellow"])}<span>Picks</span><span class="strip-sub">Tick anything wanted. Write in anything missing.</span></div>
  <div class="picks">
    <div><h3>Neighborhoods</h3>{boxes([n for n,_,_ in NEIGHBORHOODS])}</div>
    <div><h3>Foods not yet on a day</h3>{boxes([n for n,_ in FOODS[10:]])}</div>
    <div><h3>Museums not yet on a day</h3>{boxes([n for n,_ in MUSEUMS if n not in ("The Met","MoMA","The Morgan Library","Cooper Hewitt","American Museum of Natural History","The Tenement Museum","Dia Beacon","The Whitney","9/11 Memorial and Museum","The Frick")])}</div>
    <div><h3>Rituals</h3>{boxes([n for n,_ in RITUALS])}<h3 style="margin-top:1em">Anything else</h3><div class="write-lines"><div></div><div></div><div></div><div></div></div></div>
  </div>
</section>''')

# ---------- Bookings ----------
rows = "".join(f'<div class="b-row"><span class="box"></span><div class="b-name">{e(n)}</div><div class="b-when">{e(w)}</div><div class="b-note">{e(x)}</div></div>' for n,w,x in BOOKINGS)
pages.append(f'''
<section class="page prose-page">
  <div class="sign-strip">{bullet("!",L["orange"])}<span>The punch list</span><span class="strip-sub">Everything to book, buy or confirm, in order of how fast it goes. Lloyd's page.</span></div>
  <div class="grid-2 bookings">{rows}</div>
</section>''')

import os
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
CSS = open('style.css').read()
pages = [pages[0]] + [p.replace('</section>', f'<div class="pno">{i+1}</div></section>') for i,p in enumerate(pages[1:], start=1)]
doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Sarah in New York, Part Seven</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'''
open('book.html','w').write(doc)
print("pages:", len(pages))
