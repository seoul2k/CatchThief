# SingerPlayer.py
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QPoint, QRectF, QTimer, pyqtSignal
import random
import math
from Floyd import floyd_warshall

class GraphWidget_AITHEIF(QWidget):
    closed_signal = pyqtSignal()  # 定义一个信号用于通知主窗口关闭

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.generate_random_graph(30)
        self.setup_game()


    def initUI(self):
        self.setWindowTitle('警察抓小偷游戏')
        self.setGeometry(100, 100, 800, 600)

        
    def generate_random_graph(self, num_points):
        self.points = []
        width, height = self.width(), self.height()
        margin = 20
        min_distance = 60  # 增加最小距离以避免重叠

        while len(self.points) < num_points:
            x = random.randint(margin, width - margin)
            y = random.randint(margin, height - margin)
            new_point = QPoint(x, y)
            if all(self.euclidean_distance(new_point, p) >= min_distance for p in self.points):
                self.points.append(new_point)

        self.edges = set()
        self.thief_only_edges = set()
        self.police_only_edges = set()

        # 确保每个点至少连接到一个其他点（最近邻）
        for i in range(num_points):
            distances = [(j, self.euclidean_distance(self.points[i], self.points[j])) for j in range(num_points) if j != i]
            distances.sort(key=lambda x: x[1])
            nearest_neighbor = distances[0][0]
            self.edges.add((min(i, nearest_neighbor), max(i, nearest_neighbor)))

        # 添加额外的随机边
        num_edges = random.randint(40, 50)  # 随机生成边的数量
        while len(self.edges) < num_edges:
            i, j = random.sample(range(num_points), 2)
            self.edges.add((min(i, j), max(i, j)))

        # 创建邻接矩阵，默认值为 float('inf')
        self.adj_matrix = [[float('inf')] * num_points for _ in range(num_points)]
        for edge in self.edges:
            i, j = edge
            distance = self.euclidean_distance(self.points[i], self.points[j])
            self.adj_matrix[i][j] = distance
            self.adj_matrix[j][i] = distance

        # 设置普通路线权重为实际距离
        for i in range(num_points):
            for j in range(num_points):
                if (i, j) in self.edges or (j, i) in self.edges:
                    self.adj_matrix[i][j] = distance
                    self.adj_matrix[j][i] = distance

        # 设置小偷专有路线权重为实际距离
        for edge in self.thief_only_edges:
            i, j = edge
            distance = self.euclidean_distance(self.points[i], self.points[j])
            self.adj_matrix[i][j] = distance
            self.adj_matrix[j][i] = distance

        # 设置警察专有路线权重为实际距离
        for edge in self.police_only_edges:
            i, j = edge
            distance = float('inf')  # 警察专有路线权重为无穷大
            self.adj_matrix[i][j] = distance
            self.adj_matrix[j][i] = distance

        # 分配点的类型：警察起点、小偷起点、宝藏、出口
        self.point_types = ['Normal'] * num_points

        # 找到中心点附近的一个点作为宝藏点
        center_x, center_y = width // 2, height // 2
        center_point = QPoint(center_x, center_y)
        distances_to_center = [(i, self.euclidean_distance(p, center_point)) for i, p in enumerate(self.points)]
        distances_to_center.sort(key=lambda x: x[1])
        treasure_index = distances_to_center[len(distances_to_center) // 2][0]

        # 确保警察和小偷的初始位置相距较远
        police_index, thief_index = self.find_far_apart_points()
        exit_index = random.choice([i for i in range(num_points) if i not in [police_index, thief_index, treasure_index]])

        self.point_types[police_index] = 'Police Start'
        self.point_types[thief_index] = 'Thief Start'
        self.point_types[treasure_index] = 'Treasure'
        self.point_types[exit_index] = 'Exit'

        # 添加小偷专有路线和警察专有路线
        self.add_special_routes()

    def add_special_routes(self):
        num_points = len(self.points)
        num_thief_only_routes = random.randint(5, 10)  # 随机生成小偷专有路线数量
        num_police_only_routes = random.randint(5, 10)  # 随机生成警察专有路线数量

        available_edges = set(self.edges)

        for _ in range(num_thief_only_routes):
            if not available_edges:
                break
            edge = random.choice(list(available_edges))
            self.thief_only_edges.add(edge)
            available_edges.remove(edge)
            self.edges.remove(edge)

        for _ in range(num_police_only_routes):
            if not available_edges:
                break
            edge = random.choice(list(available_edges))
            self.police_only_edges.add(edge)
            available_edges.remove(edge)
            self.edges.remove(edge)

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p1.x() - p2.x()) ** 2 + (p1.y() - p2.y()) ** 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制公共边
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)
        for edge in self.edges:
            painter.drawLine(self.points[edge[0]], self.points[edge[1]])

        # 绘制小偷专有边
        thief_pen = QPen(QColor(255, 165, 0), 2, Qt.SolidLine)  # 橙色
        painter.setPen(thief_pen)
        for edge in self.thief_only_edges:
            painter.drawLine(self.points[edge[0]], self.points[edge[1]])

        # 绘制警察专有边
        police_pen = QPen(QColor(128, 0, 128), 2, Qt.SolidLine)  # 紫色
        painter.setPen(police_pen)
        for edge in self.police_only_edges:
            painter.drawLine(self.points[edge[0]], self.points[edge[1]])

        # 根据类型绘制点的不同颜色
        brushes = {
            'Normal': QColor(255, 0, 0),
            'Police Start': QColor(233, 93, 93),
            'Thief Start': QColor(87, 105, 120),
            'Treasure': QColor(93, 226, 231),
            'Exit': QColor(1, 195, 1)
        }
        point_radius = 10  # 增大圆点大小
        for i, point in enumerate(self.points):
            brush = brushes[self.point_types[i]]
            if i == self.thief_position and not self.game_over:
                brush = QColor(255, 165, 0)  # 小偷当前位置为橙色
            elif i == self.police_position and not self.game_over:
                brush = QColor(128, 0, 128)  # 警察当前位置为紫色
            elif i == self.treasure_position and self.thief_has_treasure:
                brush = QColor(255, 0, 0)  # 小偷拿到宝藏后，宝藏位置变为红色
            painter.setBrush(brush)
            painter.drawEllipse(point, point_radius, point_radius)

        # 高亮显示当前轮到移动的角色位置
        if not self.game_over:
            highlight_brush = QColor(255, 255, 255, 128)  # 半透明白色用于高亮
            painter.setBrush(highlight_brush)
            if self.current_turn == 'Thief':
                painter.drawEllipse(self.points[self.thief_position], point_radius + 2, point_radius + 2)
            else:
                painter.drawEllipse(self.points[self.police_position], point_radius + 2, point_radius + 2)

    def mousePressEvent(self, event):
        if self.game_over:
            return

        click_pos = event.pos()
        closest_point_index = self.find_closest_point(click_pos.x(), click_pos.y())

        if self.current_turn == 'Police':
            if self.is_connected(self.police_position, closest_point_index, allow_police=True):
                self.police_position = closest_point_index
                self.check_game_over()
                self.current_turn = 'Thief'
                self.ai_move_thief()

        self.update_game_state()

    def find_closest_point(self, x, y):
        closest_index = 0
        min_distance = float('inf')
        for i, point in enumerate(self.points):
            distance = self.euclidean_distance(QPoint(x, y), point)
            if distance < min_distance:
                min_distance = distance
                closest_index = i
        return closest_index

    def is_connected(self, start, end, allow_thief=False, allow_police=False):
        if allow_thief:
            # 小偷可以走普通路线和小偷专有路线
            if (start, end) in self.edges or (end, start) in self.edges:
                return True
            if ((start, end) in self.thief_only_edges or (end, start) in self.thief_only_edges):
                return True
        if allow_police:
            # 警察可以走普通路线和警察专有路线
            if (start, end) in self.edges or (end, start) in self.edges:
                return True
            if ((start, end) in self.police_only_edges or (end, start) in self.police_only_edges):
                return True
        return False

    def check_game_over(self):
        if self.police_position == self.thief_position:
            self.game_over = True
            self.winner = '警察'
            self.show_winner_message()
        elif self.thief_position == self.exit_position and self.thief_has_treasure:
            self.game_over = True
            self.winner = '小偷'
            self.show_winner_message()

    def show_winner_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("游戏结束")
        msg_box.setText(f"{self.winner}获胜！")
        msg_box.buttonClicked.connect(self.restart_or_exit)
        msg_box.exec_()

    def restart_or_exit(self):
        self.close()  # 关闭当前游戏窗口
        self.closed_signal.emit()  # 发送关闭信号给主窗口

    def show_thief_picked_up_treasure_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("宝藏已拾取")
        msg_box.setText("小偷已拾取宝藏！")
        msg_box.exec_()

    def find_far_apart_points(self):
        max_distance = 0
        police_index, thief_index = 0, 1
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = self.euclidean_distance(self.points[i], self.points[j])
                if distance > max_distance:
                    max_distance = distance
                    police_index, thief_index = i, j
        return police_index, thief_index

    def setup_game(self):
        self.thief_position = self.point_types.index('Thief Start')
        self.police_position = self.point_types.index('Police Start')
        self.treasure_position = self.point_types.index('Treasure')
        self.exit_position = self.point_types.index('Exit')

        self.current_turn = 'Police'
        self.thief_has_treasure = False
        self.game_over = False
        self.winner = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ai_move_thief)
        self.timer.start(1000)  # 每秒移动一次

        self.update_game_state()

    def update_game_state(self):
        self.repaint()

    def ai_move_thief(self):
        if self.game_over or self.current_turn != 'Thief':
            return

        # 如果小偷没有宝藏，先去拿宝藏
        if not self.thief_has_treasure:
            target_position = self.treasure_position
        else:
            target_position = self.exit_position

        # 获取所有可能的下一步位置
        possible_moves = self.get_possible_moves(self.thief_position, allow_thief=True)

        # 过滤掉终点有警察或警察相邻的位置
        safe_moves = [move for move in possible_moves if not self.is_adjacent(move, self.police_position)]

        if not safe_moves:
            # 如果没有安全的移动选项，尝试直接移动到目标位置
            safe_moves = possible_moves

        if not safe_moves:
            # 如果仍然没有移动选项，结束回合
            self.current_turn = 'Police'
            self.update_game_state()
            return

        # 使用弗洛伊德算法计算从小偷位置到目标位置的最短路径
        path = floyd_warshall(self.adj_matrix, self.thief_position, target_position)

        # 找到路径中的第一个安全节点
        next_position = None
        for node in path:
            if node in safe_moves:
                next_position = node
                break

        if next_position is None:
            # 如果找不到安全的下一个节点，选择一个随机的安全移动
            next_position = random.choice(safe_moves)

        if next_position is not None:
            if self.is_connected(self.thief_position, next_position, allow_thief=True):
                self.thief_position = next_position
                if next_position == self.treasure_position:
                    self.thief_has_treasure = True
                    self.show_thief_picked_up_treasure_message()
                    self.point_types[self.treasure_position] = 'Normal'  # 将宝藏点类型改为普通
                self.check_game_over()
                self.current_turn = 'Police'
                self.update_game_state()
            else:
                for i in self.adj_matrix[self.thief_position]:
                    if i != float("inf"):
                        self.thief_position = self.adj_matrix[self.thief_position].index(i)
                        self.check_game_over()
                        self.current_turn = 'Police'
                        self.update_game_state()
                        break                
        else:
            for i in self.adj_matrix[self.thief_position]:
                if i != float("inf"):
                    self.thief_position = self.adj_matrix[self.thief_position].index(i)
                    self.check_game_over()
                    self.current_turn = 'Police'
                    self.update_game_state()
                    break

    def get_possible_moves(self, position, allow_thief=False):
        moves = []
        for i in range(len(self.points)):
            if self.is_connected(position, i, allow_thief=allow_thief):
                moves.append(i)
        return moves

    def is_adjacent(self, position1, position2):
        return self.is_connected(position1, position2, allow_thief=True) or self.is_connected(position1, position2, allow_police=True)
            
