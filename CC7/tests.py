import unittest
import random
from solution import RoboKingOfAllCosmos, Item

random.seed(331)


class MyTestCase(unittest.TestCase):


    def test_construct_score_book_basic(self):
        king = RoboKingOfAllCosmos()

        items_scores = [('golden general', 5.1)]

        king.construct_score_book(items_scores)
        self.assertEqual([('golden general', 5.1)], king.get_score_book())

        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('long screw', 3.2), ('short screw', 2.5), ('push pin', 3.5), ('cough drop', 3.1),
         ('nail', 3.2)]

        king.construct_score_book(items_scores)
        self.assertEqual([('eyedrops', 7.3), ('long screw', 3.2), ('short screw', 2.5), ('push pin', 3.5), ('cough drop', 3.1), ('nail', 3.2)], king.get_score_book())



    def test_contruct_score_book_advanced(self):
        #Empty
        king = RoboKingOfAllCosmos()
        items_scores = []
        king.construct_score_book(items_scores)
        self.assertEqual([], king.get_score_book())

        #One
        king = RoboKingOfAllCosmos()
        items_scores = [('golden general', 5.1)]
        king.construct_score_book(items_scores)
        self.assertEqual([('golden general', 5.1)], king.get_score_book())

        #Many
        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('short screw', 2.5), ('long screw', 3.2), ('push pin', 3.5), ('red crayon', 4.2), ('cookie',6.5), ('cookie sandwich',5.8)
                            ,('button',2.5), ('lipstick', 7.6), ('mosquito',2.2), ('cherries',8), ('compass',7.1)]
        king.construct_score_book(items_scores)
        self.assertEqual([('eyedrops', 7.3), ('short screw', 2.5), ('long screw', 3.2), ('push pin', 3.5), ('red crayon', 4.2), ('cookie',6.5), ('cookie sandwich',5.8)
                            ,('button',2.5), ('lipstick', 7.6), ('mosquito',2.2), ('cherries',8), ('compass',7.1)], king.get_score_book())

        #Tests for duplicates. Two cookies in input -> one cookie in output
        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('short screw', 2.5), ('long screw', 3.2), ('push pin', 3.5),
                        ('red crayon', 4.2), ('cookie', 6.5),('cookie', 6.5), ('cookie sandwich', 5.8)
                        , ('button', 2.5), ('lipstick', 7.6), ('mosquito', 2.2), ('cherries', 8), ('compass', 7.1)]
        king.construct_score_book(items_scores)
        self.assertEqual([('eyedrops', 7.3), ('short screw', 2.5), ('long screw', 3.2), ('push pin', 3.5), ('red crayon', 4.2), ('cookie', 6.5), ('cookie sandwich', 5.8)
                          , ('button', 2.5), ('lipstick', 7.6), ('mosquito', 2.2), ('cherries', 8), ('compass', 7.1)], king.get_score_book())

        #large
        king = RoboKingOfAllCosmos()
        items_scores = [('Pedestal', '68.9'), ('Calculator', '14'), ('Iron', '43.8'), ('Eyedrops', '7.3'), ('Compass', '7.1'),
                        ('Glasses', '9.3'), ('Paperweight', '8.8'), ('India Ink', '15.6'), ('Fake Snow', '4.2'), ('Hanko', '5.1'),
                        ('Inkpad', '5.4'), ('Mosquito', '2.2'), ('Seat Cushion', '69.3'), ('Ring Box', '32.2'),
                        ('Legless Chair', '1.18'), ('Cookie Tin', '30'), ('Short Screw', '2.5'), ('Long Screw', '3.2'),
                        ('Teddy Bear', '44.5'), ('Mouse', '11.1'), ('Snail', '9.8'), ('Tree Frog', '7.4'), ('Thumbtack', '3.1'),
                        ('Pushpin', '3.5'), ('White Crayon', '5.9'), ('Black Crayon', '3.7'), ('Red Crayon', '4.2'),
                        ('Pink Crayon', '4.8'), ('Lime Crayon', '5'), ('Aqua Crayon', '5.4'), ('Brown Crayon', '5.6'), ('Beige Crayon', '5.1'),
                        ('Ochre Crayon', '5.7'), ('Gold Crayon', '5.9'), ('Die', '2.8'), ('Sausage', '8.3'), ('RC Controller', '30.1'),
                        ('Soy Sauce Pack', '5.6'), ('Thermometer', '4.9')]

        king.construct_score_book(items_scores)
        self.assertEqual([('Pedestal', '68.9'), ('Calculator', '14'), ('Iron', '43.8'), ('Eyedrops', '7.3'), ('Compass', '7.1'),
                        ('Glasses', '9.3'), ('Paperweight', '8.8'), ('India Ink', '15.6'), ('Fake Snow', '4.2'), ('Hanko', '5.1'),
                        ('Inkpad', '5.4'), ('Mosquito', '2.2'), ('Seat Cushion', '69.3'), ('Ring Box', '32.2'),
                        ('Legless Chair', '1.18'), ('Cookie Tin', '30'), ('Short Screw', '2.5'), ('Long Screw', '3.2'),
                        ('Teddy Bear', '44.5'), ('Mouse', '11.1'), ('Snail', '9.8'), ('Tree Frog', '7.4'), ('Thumbtack', '3.1'),
                        ('Pushpin', '3.5'), ('White Crayon', '5.9'), ('Black Crayon', '3.7'), ('Red Crayon', '4.2'),
                        ('Pink Crayon', '4.8'), ('Lime Crayon', '5'), ('Aqua Crayon', '5.4'), ('Brown Crayon', '5.6'), ('Beige Crayon', '5.1'),
                        ('Ochre Crayon', '5.7'), ('Gold Crayon', '5.9'), ('Die', '2.8'), ('Sausage', '8.3'), ('RC Controller', '30.1'),
                        ('Soy Sauce Pack', '5.6'), ('Thermometer', '4.9')], king.get_score_book())

    def test_judge_katamari_basic(self):

        #One
        king = RoboKingOfAllCosmos()
        items_scores = [('golden general', 5.1)]
        king.construct_score_book(items_scores)
        katamari = [Item('golden general', 'games')]
        size, top_three_cats, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(5.1, size)
        self.assertEqual([('games', 1)], top_three_cats)
        self.assertEqual([], found_cousins)

        #Many no cousins
        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('long screw', 3.2), ('short screw', 2.5), ('push pin', 3.5),
                        ('cough drop', 3.1), ('nail', 3.2)]
        king.construct_score_book(items_scores)
        katamari = [Item('eyedrops', 'necessities'), Item('long screw', 'tools'), Item('short screw', 'tools'), Item('push pin', 'stationery'),
                    Item('cough drop', 'necessities'), Item('nail', 'tools')]
        size, top_three_cats, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(22.8, size)
        self.assertEqual([('tools', 3), ('necessities', 2), ('stationery', 1)], top_three_cats)
        self.assertEqual([], found_cousins)

        #Many with cousins
        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('long screw', 3.2), ('short screw', 2.5), ('push pin', 3.5),
                        ('cough drop', 3.1), ('nail', 3.2)]
        king.construct_score_book(items_scores)
        katamari = [Item('eyedrops', 'necessities'), Item('long screw', 'tools'), Item('short screw', 'tools'),
                    Item('push pin', 'stationery'), Item('cough drop', 'necessities'), Item('nail', 'tools'),
                    Item('The Prince', 'cousins'), Item('The King Of All Cosmos', 'cousins')]
        size, top_three_cats, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(22.8, size)
        self.assertEqual([('tools', 3), ('necessities', 2), ('cousins', 2)], top_three_cats)
        self.assertEqual(['The Prince', 'The King Of All Cosmos'], found_cousins)

    def test_judge_katamari_advanced(self):
        # Empty
        king = RoboKingOfAllCosmos()
        items_scores = []
        katamari = []
        king.construct_score_book(items_scores)
        size, top_three, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(0, size)
        self.assertEqual([], top_three)
        self.assertEqual([], found_cousins)

        # Tests for duplicates. Two cookies in input -> one cookie in output
        king = RoboKingOfAllCosmos()
        items_scores = [('eyedrops', 7.3), ('short screw', 2.5), ('long screw', 3.2), ('push pin', 3.5),
                        ('red crayon', 4.2), ('cookie', 6.5), ('cookie', 6.5), ('cookie sandwich', 5.8)
                        , ('button', 2.5), ('lipstick', 7.6), ('mosquito', 2.2), ('cherries', 8), ('compass', 7.1)]
        king.construct_score_book(items_scores)
        katamari = [Item('eyedrops', 'necessities'), Item('short screw', 'tools'), Item('long screw', 'tools'), Item('push pin', 'stationery')
                    , Item('red crayon', 'stationary'), Item('cookie', 'snacks'), Item('cookie sandwich', 'snacks')
                    , Item('button', 'necessities'), Item('lipstick', 'fashion'), Item('mosquito', 'animal'), Item('cherries', 'fruit'),
                    Item('compass', 'science')]
        size, top_three_cat, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(60.4, size)
        self.assertEqual([('tools', 2), ('snacks', 2), ('necessities', 2)], top_three_cat)
        self.assertEqual([],found_cousins)




        # large
        king = RoboKingOfAllCosmos()
        items_scores = [('Pedestal', 68.9), ('Calculator', 14.0), ('Iron', 43.8), ('Eyedrops', 7.3), ('Compass', 7.1),
                        ('Glasses', 9.3), ('Paperweight', 8.8), ('India Ink', 15.6), ('Fake Snow', 4.2), ('Hanko', 5.1),
                        ('Inkpad', 5.4), ('Mosquito', 2.2), ('Seat Cushion', 69.3), ('Ring Box', 32.2), ('Legless Chair', 118.0),
                        ('Cookie Tin', 30.0), ('Short Screw', 2.5), ('Long Screw', 3.2), ('Teddy Bear', 44.5), ('Mouse', 11.1),
                        ('Snail', 9.8), ('Tree Frog', 7.4), ('Thumbtack', 3.1), ('Pushpin', 3.5), ('Pushpin', 3.5),
                        ('White Crayon', 5.9), ('Black Crayon', 3.7), ('Red Crayon', 4.2), ('Pink Crayon', 4.8),
                        ('Lime Crayon', 5.0), ('Aqua Crayon', 5.4), ('Brown Crayon', 5.6), ('Beige Crayon', 5.1),
                        ('Ochre Crayon', 5.7), ('Gold Crayon', 5.9), ('Die', 2.8), ('Sausage', 8.3), ('RC Controller', 30.1),
                        ('Soy Sauce Pack', 5.6), ('Thermometer', 4.9)]

        king.construct_score_book(items_scores)
        katamari = [Item('Pedestal','decorations'), Item('Calculator','electronics'), Item('Iron','electronics'),
                    Item('Eyedrops','necessities'), Item('Compass','science'), Item('Glasses','fashion'), Item('Paperweight','stationery'),
                    Item('India Ink','stationery'), Item('Fake Snow','decorations'), Item('Hanko','necessities'), Item('Inkpad','necessities'),
                    Item('Mosquito','animals'), Item('Seat Cushion','seating'), Item('Ring Box','containers'), Item('Legless Chair','seating'),
                    Item('Cookie Tin','containers'), Item('Short Screw','tools'), Item('Long Screw','tools'), Item('Teddy Bear','cute'),
                    Item('Mouse','animals'), Item('Snail','rain'), Item('Tree Frog','rain'), Item('Thumbtack','stationery'),
                    Item('Pushpin','stationery'), Item('Pushpin','stationery'), Item('White Crayon','stationery'),
                    Item('Black Crayon','stationery'), Item('Red Crayon','stationery'), Item('Pink Crayon','stationery'),
                    Item('Lime Crayon','stationery'), Item('Aqua Crayon','stationery'), Item('Brown Crayon','stationery'),
                    Item('Beige Crayon','stationery'), Item('Ochre Crayon','stationery'), Item('Gold Crayon','stationery'),
                    Item('Die','games'), Item('Sausage','food'), Item('RC Controller','control'), Item('Soy Sauce Pack','containers'),
                    Item('Thermometer','measuring')]

        size, top_three_cat, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(632.8, size)
        self.assertEqual([('stationery', 15), ('necessities', 3), ('containers', 3)], top_three_cat)
        self.assertEqual([], found_cousins)

        #All cousins
        king = RoboKingOfAllCosmos()
        items_scores = [('Pedestal', 68.9), ('Calculator', 14.0), ('Iron', 43.8), ('Eyedrops', 7.3), ('Compass', 7.1),
                        ('Glasses', 9.3), ('Paperweight', 8.8), ('India Ink', 15.6), ('Fake Snow', 4.2), ('Hanko', 5.1),
                        ('Inkpad', 5.4), ('Mosquito', 2.2), ('Seat Cushion', 69.3), ('Ring Box', 32.2),
                        ('Legless Chair', 118.0),
                        ('Cookie Tin', 30.0), ('Short Screw', 2.5), ('Long Screw', 3.2), ('Teddy Bear', 44.5),
                        ('Mouse', 11.1),
                        ('Snail', 9.8), ('Tree Frog', 7.4), ('Thumbtack', 3.1), ('Pushpin', 3.5), ('Pushpin', 3.5),
                        ('White Crayon', 5.9), ('Black Crayon', 3.7), ('Red Crayon', 4.2), ('Pink Crayon', 4.8),
                        ('Lime Crayon', 5.0), ('Aqua Crayon', 5.4), ('Brown Crayon', 5.6), ('Beige Crayon', 5.1),
                        ('Ochre Crayon', 5.7), ('Gold Crayon', 5.9), ('Die', 2.8), ('Sausage', 8.3),
                        ('RC Controller', 30.1),
                        ('Soy Sauce Pack', 5.6), ('Thermometer', 4.9)]

        katamari = [Item('The Prince', 'cousins'), Item('Ace', 'cousins'), Item('Colombo', 'cousins'), Item('Dipp', 'cousins'),
                    Item('Foomin', 'cousins'), Item('Fujio', 'cousins'), Item('Havana', 'cousins'), Item('Honey', 'cousins'),
                    Item('Ichigo', 'cousins'), Item('Johnson', 'cousins'), Item('June', 'cousins'), Item('Jungle', 'cousins'),
                    Item('Kuro', 'cousins'), Item('Lalala', 'cousins'), Item('Marcy', 'cousins'), Item('Marny', 'cousins'),
                    Item('Miso', 'cousins'), Item('Nickel', 'cousins'), Item('Nik', 'cousins'), Item('Odeko', 'cousins'),
                    Item('Opeo', 'cousins'), Item('Peso', 'cousins'), Item('Shikao', 'cousins'), Item('Velvet', 'cousins')]
        size, top_three, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(0, size)
        self.assertEqual([('cousins', 24)], top_three)
        self.assertEqual(['The Prince', 'Ace', 'Colombo', 'Dipp','Foomin', 'Fujio','Havana', 'Honey',
                         'Ichigo', 'Johnson', 'June', 'Jungle','Kuro', 'Lalala', 'Marcy', 'Marny',
                          'Miso', 'Nickel', 'Nik', 'Odeko','Opeo', 'Peso', 'Shikao', 'Velvet'], found_cousins)

    def test_large_random(self):
        king = RoboKingOfAllCosmos()
        score_book = [('Pedestal', 68.9), ('Calculator', 14.0), ('Iron', 43.8), ('Eyedrops', 7.3), ('Compass', 7.1),
                      ('Glasses', 9.3), ('Paperweight', 8.8), ('India Ink', 15.6), ('Fake Snow', 4.2), ('Hanko', 5.1),
                      ('Inkpad', 5.4), ('Mosquito', 2.2), ('Seat Cushion', 69.3), ('Ring Box', 32.2), ('Legless Chair', 118.0),
                      ('Cookie Tin', 30.0), ('Short Screw', 2.5), ('Long Screw', 3.2), ('Teddy Bear', 44.5), ('Mouse', 11.1),
                      ('Snail', 9.8), ('Tree Frog', 7.4), ('Thumbtack', 3.1), ('Pushpin', 3.5), ('Pushpin', 3.5), ('White Crayon', 5.9),
                      ('Black Crayon', 3.7), ('Red Crayon', 4.2), ('Pink Crayon', 4.8), ('Lime Crayon', 5.0), ('Aqua Crayon', 5.4),
                      ('Brown Crayon', 5.6), ('Beige Crayon', 5.1), ('Ochre Crayon', 5.7), ('Gold Crayon', 5.9), ('Die', 2.8),
                      ('Sausage', 8.3), ('RC Controller', 30.1), ('Soy Sauce Pack', 5.6), ('Thermometer', 4.9), ('Stamp', 2.0),
                      ('Newspaper', 21.5), ('Leaflet', 16.8), ('Caramel Box', 11.3), ('Caramel', 4.4), ('Gum (Pack)', 8.5),
                      ('Gum', 4.5), ('Pencil Sharpener', 30.0), ('B Pencil', 4.3), ('#2 Pencil', 4.1), ('Battery', 9.8),
                      ('9-Volt Battery', 7.4), ('Nail Clipper', 12.5), ('Cookie', 6.5), ('Cookie Sandwich', 5.8), ('Hairpin', 4.5),
                      ('Ballpoint Pen', 6.5), ('Inkbrush', 8.4), ('Button', 2.5), ('Red Block', 7.0), ('Yellow Block', 8.0),
                      ('Green Block', 8.8), ('Lipstick', 7.6), ('Light Bulb', 20.8), ('Heirloom', 21.3), ('Video Game', 38.7),
                      ('Memory Card', 6.2), ('Ironing Board', 110.0), ('Pants', 140.0), ('Fruit Basket', 38.8),
                      ('Cuckoo Clock', 63.7), ('Katana', 59.0), ('Manderin Carton', 79.9), ('Pencil Stand', 18.7),
                      ('Chocolate', 4.1), ('Cabinet', 120.0), ('Drawer', 59.1), ('Switch', 7.3), ('Bookstand', 42.1),
                      ('Ruler', 28.1), ('Desk Lamp', 63.8), ('Hook', 13.5), ('Parsley', 8.0), ('Sticky Tape', 11.6),
                      ('Hanging Scroll', 60.8), ('Check Book', 10.4), ('Picture Frame', 24.8), ('Salmon', 16.5),
                      ('Cell Phone', 10.3), ('Chestnut', 4.2), ('Pachinko Ball', 4.7), ('Cheese', 8.6), ('Mousetrap', 19.5),
                      ('Mosquito Coil', 26.9), ('Mosquito Zapper', 16.8), ('Zapper Refill', 3.0), ('Cuckoo', 12.5), ('Eraser', 8.1),
                      ('Hard Eraser', 7.4), ('Weekly Magazine', 30.0), ('Dictionary', 27.0), ('Comic', 28.7), ('Diary', 19.4),
                      ('Paperback', 13.9), ('Encyclopedia', 35.8), ('Math Workbook', 16.2), ('Power Plug', 7.2),
                      ('Kotatsu Plug', 7.2), ('Power Strip', 10.6), ('Small Sliding Door', 110.0), ('Tissues', 34.5),
                      ('Wallet', 24.6), ('5 Yen Coin', 2.9), ('500 Yen Coin', 4.0), ('Foreign Coin', 3.6), ('Gold Coin', 3.8),
                      ('Matchbox', 6.9), ('Match', 1.6), ('Mandarin Piece', 6.5), ('Mandarin Peel', 14.2), ('Mandarin', 14.1),
                      ('Ant', 1.5), ('Horseshoe Crab', 50.5), ('Teacup', 18.0), ('Cassette Tape', 9.7), ('Boombox', 62.3),
                      ('Soda', 17.0), ('Dustbin', 53.0), ('Mini Pylon', 10.0), ('Candy', 6.0), ('Milk Candy', 6.0),
                      ('Mah-Jong Tile', 5.1), ('Mah-Jong Tile', 5.1), ('Mah-Jong Tile', 5.1), ('Mah-Jong Tile', 5.1),
                      ('"""Over 10cm"" Sign"', 10.0), ('Plate', 30.8), ('Square Dish', 24.0),
                      ('Chopsticks', 8.8), ('Shumai Dumpling', 12.3), ('Emerald Ring', 7.3), ('Sapphire Ring', 7.3),
                      ('Diamond Ring', 7.3)]
        king.construct_score_book(score_book)
        available_items = [Item('Pedestal','decorations'), Item('Calculator','electronics'), Item('Iron','electronics'),
                           Item('Eyedrops','necessities'), Item('Compass','science'), Item('Glasses','fashion'),
                           Item('Paperweight','stationery'), Item('India Ink','stationery'), Item('Fake Snow','decorations'),
                           Item('Hanko','necessities'), Item('Inkpad','necessities'), Item('Mosquito','animals'),
                           Item('Seat Cushion','seating'), Item('Ring Box','containers'), Item('Legless Chair','seating'),
                           Item('Cookie Tin','containers'), Item('Short Screw','tools'), Item('Long Screw','tools'),
                           Item('Teddy Bear','cute'), Item('Mouse','animals'), Item('Snail','rain'), Item('Tree Frog','rain'),
                           Item('Thumbtack','stationery'), Item('Pushpin','stationery'), Item('Pushpin','stationery'),
                           Item('White Crayon','stationery'), Item('Black Crayon','stationery'), Item('Red Crayon','stationery'),
                           Item('Pink Crayon','stationery'), Item('Lime Crayon','stationery'), Item('Aqua Crayon','stationery'),
                           Item('Brown Crayon','stationery'), Item('Beige Crayon','stationery'), Item('Ochre Crayon','stationery'),
                           Item('Gold Crayon','stationery'), Item('Die','games'), Item('Sausage','food'),
                           Item('RC Controller','control'), Item('Soy Sauce Pack','containers'), Item('Thermometer','measuring'),
                           Item('Stamp','post'), Item('Newspaper','post'), Item('Leaflet','post'), Item('Caramel Box','snacks'),
                           Item('Caramel','snacks'), Item('Gum (Pack)','snacks'), Item('Gum','snacks'),
                           Item('Pencil Sharpener','stationery'), Item('B Pencil','stationery'), Item('#2 Pencil','stationery'),
                           Item('Battery','energy'), Item('9-Volt Battery','energy'), Item('Nail Clipper','necessities'),
                           Item('Cookie','snacks'), Item('Cookie Sandwich','snacks'), Item('Hairpin','fashion'),
                           Item('Ballpoint Pen','stationery'), Item('Inkbrush','stationery'), Item('Button','necessities'),
                           Item('Red Block','playtime'), Item('Yellow Block','playtime'), Item('Green Block','playtime'),
                           Item('Lipstick','fashion'), Item('Light Bulb','lighting'), Item('Heirloom','guidance'),
                           Item('Video Game','games'), Item('Memory Card','electronics'), Item('Ironing Board','furniture'),
                           Item('Pants','cleaning'), Item('Fruit Basket','containers'), Item('Cuckoo Clock','electronics'),
                           Item('Katana','weapons'), Item('Manderin Carton','furniture'), Item('Pencil Stand','stationery'),
                           Item('Chocolate','snacks'), Item('Cabinet','furniture'), Item('Drawer','furniture'),
                           Item('Switch','control'), Item('Bookstand','furniture'), Item('Ruler','measuring'),
                           Item('Desk Lamp','lighting'), Item('Hook','necessities'), Item('Parsley','decorations'),
                           Item('Sticky Tape','stationery'), Item('Hanging Scroll','art'), Item('Check Book','rich'),
                           Item('Picture Frame','decorations'), Item('Salmon','japanese food'), Item('Cell Phone','communication'),
                           Item('Chestnut','snacks'), Item('Pachinko Ball','games'), Item('Cheese','food'),
                           Item('Mousetrap','danger'), Item('Mosquito Coil','summer'), Item('Mosquito Zapper','summer'),
                           Item('Zapper Refill','summer'), Item('Cuckoo','wings'), Item('Eraser','stationery'),
                           Item('Hard Eraser','stationery'), Item('Weekly Magazine','reading'), Item('Dictionary','reading'),
                           Item('Comic','reading'), Item('Diary','reading'), Item('Paperback','reading'),
                           Item('Encyclopedia','reading'), Item('Math Workbook','reading'), Item('Power Plug','energy'),
                           Item('Kotatsu Plug','energy'), Item('Power Strip','energy'),
                           Item('Small Sliding Door','entrances & exits'), Item('Tissues','necessities'),
                           Item('Wallet','containers'), Item('5 Yen Coin','rich'), Item('500 Yen Coin','rich'),
                           Item('Foreign Coin','rich'), Item('Gold Coin','rich'), Item('Matchbox','necessities'),
                           Item('Match','necessities'), Item('Mandarin Piece','fruit'), Item('Mandarin Peel','trash'),
                           Item('Mandarin','fruit'), Item('Ant','workers'), Item('Horseshoe Crab','aquarium'),
                           Item('Teacup','drinks'), Item('Cassette Tape','sound'), Item('Boombox','sound'),
                           Item('Soda','drinks'), Item('Dustbin','trash'), Item('Mini Pylon','danger'), Item('Candy','snacks'),
                           Item('Milk Candy','snacks'), Item('Mah-Jong Tile','games'), Item('Mah-Jong Tile','games'),
                           Item('Mah-Jong Tile','games'), Item('Mah-Jong Tile','games'), Item('"""Over 10cm"" Sign"','guidance'),
                           Item('Havana','cousins'), Item('Marcy','cousins'), Item('Plate','cooking'),
                           Item('Square Dish','cooking'), Item('Chopsticks','cooking'), Item('Shumai Dumpling','food'),
                           Item('Emerald Ring','rich'), Item('Sapphire Ring','rich'), Item('Diamond Ring','rich')]
        katamari = []
        for i in range(0, 1000):
            katamari.append(available_items[random.randrange(0, len(available_items))])

        size, top_three, found_cousins = king.judge_katamari(katamari)
        self.assertEqual(19617.1, size)
        self.assertEqual([('stationery', 157), ('snacks', 82), ('necessities', 63)], top_three)
        self.assertEqual(['Marcy', 'Havana', 'Marcy', 'Marcy', 'Havana', 'Marcy', 'Marcy', 'Marcy', 'Havana', 'Havana',
                          'Havana', 'Marcy'], found_cousins)


if __name__ == '__main__':
    unittest.main()