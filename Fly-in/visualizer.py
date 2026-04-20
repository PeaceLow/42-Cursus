import tkinter as tk
from typing import Dict, Tuple
from simulation import Simulation


class MapVisualizer:
    """
    Graphical interface for visualizing the map and drone movements.
    """

    def __init__(self, simulation: Simulation) -> None:
        """
        Initializes the visualizer with a given simulation.
        """
        self.sim = simulation
        self.graph = simulation.graph

        self.root = tk.Tk()
        self.root.title("Fly-in Drone Simulation Visualizer")
        self.root.configure(bg="#2b2b2b")

        self.canvas_width = 800
        self.canvas_height = 600
        self.padding = 60

        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="#1e1e1e",
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.turn_lbl = tk.Label(
            self.root,
            text="Turn: 0",
            font=("Segoe UI", 16, "bold"),
            bg="#2b2b2b",
            fg="#ffffff"
        )
        self.turn_lbl.pack(pady=5)

        controls = tk.Frame(self.root, bg="#2b2b2b")
        controls.pack(pady=10)

        btn_style = {
            "font": ("Segoe UI", 11, "bold"),
            "bg": "#4a4a4a",
            "fg": "#ffffff",
            "activebackground": "#626262",
            "activeforeground": "#ffffff",
            "relief": tk.FLAT,
            "padx": 15,
            "pady": 5,
            "cursor": "hand2"
        }

        tk.Button(controls, text="|<< Start", command=self.reset_turn, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(controls, text="<< Prev", command=self.prev_turn, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(controls, text="Play", command=self.play, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(controls, text="Pause", command=self.pause, **btn_style).pack(side=tk.LEFT, padx=10)
        tk.Button(controls, text="Next >>", command=self.next_turn, **btn_style).pack(side=tk.LEFT, padx=10)

        # Speed slider
        speed_frame = tk.Frame(controls, bg="#2b2b2b")
        speed_frame.pack(side=tk.LEFT, padx=15)
        tk.Label(speed_frame, text="Speed", bg="#2b2b2b", fg="#ffffff", font=("Segoe UI", 10)).pack(side=tk.TOP)
        self.speed_scale = tk.Scale(speed_frame, from_=0.01, to=0.5, resolution=0.01, orient=tk.HORIZONTAL,
                                    bg="#2b2b2b", fg="#ffffff", highlightthickness=0, length=120)
        self.speed_scale.set(0.05)
        self.speed_scale.pack(side=tk.BOTTOM)

        self.current_turn = 0
        self.max_turn = 0

        for sched in self.sim.instructions.values():
            if sched:
                self.max_turn = max(self.max_turn, sched[-1][0])

        self.is_playing = False

        self._calc_scales()
        self.node_positions: Dict[str, Tuple[float, float]] = {}

        self.drone_items: Dict[int, int] = {}

        self.draw_static_map()
        self.update_drones()

        self.canvas.bind("<Configure>", self.on_resize)

    def on_resize(self, event: tk.Event) -> None:
        """
        Handles canvas resize events.
        """
        if (
            event.width == self.canvas_width
            and event.height == self.canvas_height
        ):
            return

        self.canvas_width = event.width
        self.canvas_height = event.height

        self.canvas.delete("all")
        self.drone_items.clear()

        self._calc_scales()
        self.draw_static_map()
        self.update_drones()

    def _calc_scales(self) -> None:
        xs = [z.x for z in self.graph.zones.values()]
        ys = [z.y for z in self.graph.zones.values()]

        if not xs or not ys:
            self.min_x = self.max_x = self.min_y = self.max_y = 0
            self.scale_x = self.scale_y = 1.0
            return

        self.min_x, self.max_x = min(xs), max(xs)
        self.min_y, self.max_y = min(ys), max(ys)

        dx = max(1, self.max_x - self.min_x)
        dy = max(1, self.max_y - self.min_y)

        usable_w = self.canvas_width - 2 * self.padding
        usable_h = self.canvas_height - 2 * self.padding

        self.scale_x = usable_w / dx
        self.scale_y = usable_h / dy

    def transform(self, x: float, y: float) -> Tuple[float, float]:
        """
        Converts graph coordinates to canvas coordinates.
        """
        cx = self.padding + (x - self.min_x) * self.scale_x
        cy = self.padding + (y - self.min_y) * self.scale_y
        return cx, cy

    def draw_static_map(self) -> None:
        """
        Draws the zones and connections on the canvas.
        """
        # Draw connections
        for conn in self.graph.connections:
            x1, y1 = self.transform(conn.zone1.x, conn.zone1.y)
            x2, y2 = self.transform(conn.zone2.x, conn.zone2.y)
            dashes: Tuple[int, ...] | str = ""
            if (conn.zone1.zone_type == "restricted" or
                    conn.zone2.zone_type == "restricted"):
                dashes = (4, 4)

            self.canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill="#5c6bc0",
                width=max(
                    1,
                    conn.max_link_capacity *
                    1.5),
                dash=dashes)

        # Draw zones
        r = 18
        for zone in self.graph.zones.values():
            cx, cy = self.transform(zone.x, zone.y)
            self.node_positions[zone.name] = (cx, cy)

            color = zone.color if zone.color else "white"
            try:
                # Test color validity
                self.canvas.winfo_rgb(color)
            except tk.TclError:
                color = "#bbbbbb"

            outline = "#1e1e1e"
            width = 2
            if zone == self.graph.start_zone:
                outline = "#4CAF50"
                width = 4
            elif zone == self.graph.end_zone:
                outline = "#F44336"
                width = 4

            # Shadow
            self.canvas.create_oval(
                cx - r + 3, cy - r + 3, cx + r + 3, cy + r + 3,
                fill="#151515", outline=""
            )
            # Main oval
            self.canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r,
                fill=color, outline=outline, width=width
            )
            
            # Helper to draw text with a background to avoid unreadable overlays
            def draw_text_with_bg(x: float, y: float, txt: str, fnt: tuple, fg: str, bg: str):
                text_item = self.canvas.create_text(x, y, text=txt, font=fnt, fill=fg)
                bbox = self.canvas.bbox(text_item)
                if bbox:
                    # Padding
                    rect_item = self.canvas.create_rectangle(
                        bbox[0]-2, bbox[1]-1, bbox[2]+2, bbox[3]+1,
                        fill=bg, outline="", tags="bg"
                    )
                    self.canvas.tag_lower(rect_item, text_item)

            draw_text_with_bg(
                cx, cy - r - 15,
                txt=zone.name,
                fnt=("Segoe UI", 10, "bold"),
                fg="#ffffff", bg="#1e1e1e"
            )
            if zone.max_drones > 1:
                draw_text_with_bg(
                    cx, cy + r + 15,
                    txt=f"Cap: {zone.max_drones}",
                    fnt=("Segoe UI", 9),
                    fg="#cccccc", bg="#1e1e1e"
                )

    def _get_target_pos(self, target: str) -> Tuple[float, float]:
        """
        Returns the exact (x, y) target coordinates.
        """
        if "-" in target:
            z1, z2 = target.split("-", 1)
            x1, y1 = self.node_positions.get(z1, (0.0, 0.0))
            x2, y2 = self.node_positions.get(z2, (0.0, 0.0))
            return (x1 + x2) / 2, (y1 + y2) / 2
        elif target in self.node_positions:
            return self.node_positions[target]
        return 0.0, 0.0

    def get_drone_position(self, drone_id: int,
                           turn: float) -> Tuple[float, float]:
        """
        Interpolates drone position for a continuous fractional turn.
        """
        if not self.graph.start_zone:
            return 0.0, 0.0

        sched = self.sim.instructions.get(drone_id, [])
        if not sched:
            return self.node_positions[self.graph.start_zone.name]

        # Insert start segment
        full_sched = [(0, self.graph.start_zone.name)] + sched

        if turn <= 0:
            return self._get_target_pos(full_sched[0][1])
        if turn >= full_sched[-1][0]:
            return self._get_target_pos(full_sched[-1][1])

        for i in range(len(full_sched) - 1):
            t1, tg1 = full_sched[i]
            t2, tg2 = full_sched[i + 1]

            if t1 <= turn <= t2:
                if t1 == t2:
                    return self._get_target_pos(tg2)

                ratio = (turn - t1) / (t2 - t1)
                
                # Easing function for smoother movement (ease in-out)
                ratio_eased = ratio * ratio * (3 - 2 * ratio)

                p1 = self._get_target_pos(tg1)
                p2 = self._get_target_pos(tg2)

                x = p1[0] + (p2[0] - p1[0]) * ratio_eased
                y = p1[1] + (p2[1] - p1[1]) * ratio_eased
                return x, y

        return self._get_target_pos(full_sched[-1][1])

    def update_drones(self) -> None:
        """
        Updates the canvas with new drone positions.
        """
        # Affichage du tour en tant qu'entier
        display_turn = int(self.current_turn)
        if self.current_turn > 0 and self.current_turn == self.max_turn:
            display_turn = self.max_turn
            
        self.turn_lbl.config(
            text=f"Turn: {display_turn} / {self.max_turn}")

        dr = 10
        colors = ["#ffc107", "#03a9f4", "#e91e63", "#00bcd4", "#8bc34a", "#ff9800", "#9c27b0", "#cddc39"]

        for drone_id in range(1, self.graph.nb_drones + 1):
            cx, cy = self.get_drone_position(drone_id, self.current_turn)

            # small offset for overlapping drones
            offset_x = (drone_id % 3) * 6 - 6
            offset_y = ((drone_id // 3) % 3) * 6 - 6
            cx += offset_x
            cy += offset_y

            color = colors[drone_id % len(colors)]

            if drone_id in self.drone_items:
                self.canvas.coords(
                    self.drone_items[drone_id],
                    cx - dr, cy - dr, cx + dr, cy + dr
                )
                self.canvas.tag_raise(self.drone_items[drone_id])
            else:
                item = self.canvas.create_oval(
                    cx - dr, cy - dr, cx + dr, cy + dr,
                    fill=color, outline="#ffffff", width=2
                )
                self.drone_items[drone_id] = item

    def next_turn(self) -> None:
        """Sauts manuels entiers vers l'avant."""
        if self.current_turn < self.max_turn:
            self.current_turn = int(self.current_turn) + 1
            if self.current_turn > self.max_turn:
                self.current_turn = self.max_turn
            self.update_drones()

    def prev_turn(self) -> None:
        """Sauts manuels entiers vers l'arrière."""
        if self.current_turn > 0:
            if self.current_turn == int(self.current_turn):
                self.current_turn = max(0.0, float(int(self.current_turn) - 1))
            else:
                self.current_turn = float(int(self.current_turn))
            self.update_drones()

    def reset_turn(self) -> None:
        """Retourne au tout premier tour."""
        self.current_turn = 0.0
        self.update_drones()

    def play(self) -> None:
        if not self.is_playing:
            self.is_playing = True
            # Si on est à la fin, on relance depuis le début
            if self.current_turn >= self.max_turn:
                self.current_turn = 0.0
            self._auto_step()

    def pause(self) -> None:
        self.is_playing = False

    def _auto_step(self) -> None:
        if self.is_playing and self.current_turn < self.max_turn:
            # Incrément fractionnaire pour l'animation dépendant du curseur de vitesse
            speed = self.speed_scale.get()
            self.current_turn += speed
            if self.current_turn > self.max_turn:
                self.current_turn = self.max_turn
                
            self.update_drones()
            
            if self.current_turn < self.max_turn:
                self.root.after(25, self._auto_step)
            else:
                self.is_playing = False
        else:
            self.is_playing = False

    def show(self) -> None:
        """
        Starts the Tkinter main loop.
        """
        self.root.mainloop()
