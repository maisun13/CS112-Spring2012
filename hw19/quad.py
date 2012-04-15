
from math import ceil, floor

import pygame
from pygame.locals import *

from pygame import Rect

MAX_DEPTH = 10
class QuadTreeNode(object):

    def __init__(self, rect, depth = 0):
        self.rect = rect
        self.data = None
        self.is_split = False

        self.ne = None
        self.nw = None
        self.se = None
        self.sw = None

        self.depth = depth

    def add_point(self, point):
        # if we don't have data, just add it
        if self.data is None and not self.is_split:
            self.data = point
            return
        elif self.depth == MAX_DEPTH:
            self.data = point
            return

        # if already haven't split, do that now
        if not self.is_split:
            prev_point = self.data
            self.is_split = True

            r = self.rect
            w = self.rect.width / 2.0
            h = self.rect.height / 2.0
            d = self.depth + 1

            self.nw = QuadTreeNode( Rect(r.left, r.top, floor(w), floor(h) ), d )
            self.ne = QuadTreeNode( Rect(r.centerx, r.top, ceil(w), floor(h) ), d ) 
            self.sw = QuadTreeNode( Rect(r.left, r.centery, floor(w), ceil(h) ), d )
            self.se = QuadTreeNode( Rect(r.centerx, r.centery, ceil(w), ceil(h) ), d )

            # re add the point
            self.add_point(prev_point)

        # add the point to the split
        if self.nw.rect.collidepoint(point):
            self.nw.add_point(point)
        elif self.ne.rect.collidepoint(point):
            self.ne.add_point(point)
        elif self.sw.rect.collidepoint(point):
            self.sw.add_point(point)
        else:
            self.se.add_point(point)

    def get_points(self):
        all_points = []
        if self.data is not None:
            all_points.append(self.data)

        if self.nw and self.nw.data is not None:
            for point in self.nw.get_points():
                if point != self.data:
                    all_points.append(point)

        if self.ne and self.ne.data is not None:
            for point in self.ne.get_points():
                if point != self.data:
                    all_points.append(point)

        if self.sw and self.sw.data is not None:
            for point in self.sw.get_points():
                if point != self.data:
                    all_points.append(point)

        if self.se and self.se.data is not None:
            for point in self.se.get_points():
                if point != self.data:
                    all_points.append(point)

        return all_points
    
    def get_rects(self):
        all_rects = []
        all_rects.append(self.rect)

        if self.nw is not None:
           for rect in self.nw.get_rects():
               if not rect in all_rects:
                   all_rects.append(rect)

        if self.sw is not None:
           for rect in self.sw.get_rects():
               if not rect in all_rects:
                   all_rects.append(rect)

        if self.ne is not None:
           for rect in self.ne.get_rects():
               if not rect in all_rects:
                   all_rects.append(rect)

        if self.se is not None:
           for rect in self.se.get_rects():
               if not rect in all_rects:
                   all_rects.append(rect)

        return all_rects

