import math as python_lib_Math
import math as Math
import functools as python_lib_Functools
import inspect as python_lib_Inspect
import json as python_lib_Json
from io import StringIO as python_lib_io_StringIO


class _hx_AnonObject:
	def __init__(self, fields):
		self.__dict__ = fields


class Enum:
	_hx_class_name = "Enum"
	_hx_fields = ["tag", "index", "params"]
	_hx_methods = ["__str__"]

	def __init__(self,tag,index,params):
		self.tag = None
		self.index = None
		self.params = None
		self.tag = tag
		self.index = index
		self.params = params

	def __str__(self):
		if (self.params is None):
			return self.tag
		else:
			return (((HxOverrides.stringOrNull(self.tag) + "(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in self.params]))) + ")")

Enum._hx_class = Enum


class Alignment:
	_hx_class_name = "Alignment"
	_hx_fields = ["map_a2b", "map_b2a", "ha", "hb", "ta", "tb", "ia", "ib", "map_count", "order_cache", "order_cache_has_reference", "index_columns", "reference", "meta"]
	_hx_methods = ["range", "tables", "headers", "setRowlike", "link", "addIndexColumns", "getIndexColumns", "a2b", "b2a", "count", "toString", "toOrder", "addToOrder", "getSource", "getTarget", "getSourceHeader", "getTargetHeader", "toOrder3"]

	def __init__(self):
		self.map_a2b = None
		self.map_b2a = None
		self.ha = None
		self.hb = None
		self.ta = None
		self.tb = None
		self.ia = None
		self.ib = None
		self.map_count = None
		self.order_cache = None
		self.order_cache_has_reference = None
		self.index_columns = None
		self.reference = None
		self.meta = None
		self.map_a2b = haxe_ds_IntMap()
		self.map_b2a = haxe_ds_IntMap()
		def _hx_local_0():
			self.hb = 0
			return self.hb
		self.ha = _hx_local_0()
		self.map_count = 0
		self.reference = None
		self.meta = None
		self.order_cache_has_reference = False
		self.ia = -1
		self.ib = -1

	def range(self,ha,hb):
		self.ha = ha
		self.hb = hb

	def tables(self,ta,tb):
		self.ta = ta
		self.tb = tb

	def headers(self,ia,ib):
		self.ia = ia
		self.ib = ib

	def setRowlike(self,flag):
		pass

	def link(self,a,b):
		self.map_a2b.set(a,b)
		self.map_b2a.set(b,a)
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.map_count
		_hx_local_0.map_count = (_hx_local_1 + 1)
		_hx_local_1

	def addIndexColumns(self,unit):
		if (self.index_columns is None):
			self.index_columns = list()
		_this = self.index_columns
		_this.append(unit)

	def getIndexColumns(self):
		return self.index_columns

	def a2b(self,a):
		return self.map_a2b.h.get(a,None)

	def b2a(self,b):
		return self.map_b2a.h.get(b,None)

	def count(self):
		return self.map_count

	def toString(self):
		return ("" + HxOverrides.stringOrNull(self.map_a2b.toString()))

	def toOrder(self):
		if (self.order_cache is not None):
			if (self.reference is not None):
				if (not self.order_cache_has_reference):
					self.order_cache = None
		if (self.order_cache is None):
			self.order_cache = self.toOrder3()
		if (self.reference is not None):
			self.order_cache_has_reference = True
		return self.order_cache

	def addToOrder(self,l,r,p = -2):
		if (p is None):
			p = -2
		if (self.order_cache is None):
			self.order_cache = Ordering()
		self.order_cache.add(l,r,p)
		self.order_cache_has_reference = (p != -2)

	def getSource(self):
		return self.ta

	def getTarget(self):
		return self.tb

	def getSourceHeader(self):
		return self.ia

	def getTargetHeader(self):
		return self.ib

	def toOrder3(self):
		ref = self.reference
		if (ref is None):
			ref = Alignment()
			ref.range(self.ha,self.ha)
			ref.tables(self.ta,self.ta)
			_g1 = 0
			_g = self.ha
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				ref.link(i,i)
		order = Ordering()
		if (self.reference is None):
			order.ignoreParent()
		xp = 0
		xl = 0
		xr = 0
		hp = self.ha
		hl = ref.hb
		hr = self.hb
		vp = haxe_ds_IntMap()
		vl = haxe_ds_IntMap()
		vr = haxe_ds_IntMap()
		_g2 = 0
		while (_g2 < hp):
			i1 = _g2
			_g2 = (_g2 + 1)
			vp.set(i1,i1)
		_g3 = 0
		while (_g3 < hl):
			i2 = _g3
			_g3 = (_g3 + 1)
			vl.set(i2,i2)
		_g4 = 0
		while (_g4 < hr):
			i3 = _g4
			_g4 = (_g4 + 1)
			vr.set(i3,i3)
		ct_vp = hp
		ct_vl = hl
		ct_vr = hr
		prev = -1
		ct = 0
		max_ct = ((((hp + hl) + hr)) * 10)
		while (((ct_vp > 0) or ((ct_vl > 0))) or ((ct_vr > 0))):
			ct = (ct + 1)
			if (ct > max_ct):
				print(str("Ordering took too long, something went wrong"))
				break
			if (xp >= hp):
				xp = 0
			if (xl >= hl):
				xl = 0
			if (xr >= hr):
				xr = 0
			if ((xp < hp) and ((ct_vp > 0))):
				if ((self.a2b(xp) is None) and ((ref.a2b(xp) is None))):
					if xp in vp.h:
						order.add(-1,-1,xp)
						prev = xp
						vp.remove(xp)
						ct_vp = (ct_vp - 1)
					xp = (xp + 1)
					continue
			zl = None
			zr = None
			if ((xl < hl) and ((ct_vl > 0))):
				zl = ref.b2a(xl)
				if (zl is None):
					if xl in vl.h:
						order.add(xl,-1,-1)
						vl.remove(xl)
						ct_vl = (ct_vl - 1)
					xl = (xl + 1)
					continue
			if ((xr < hr) and ((ct_vr > 0))):
				zr = self.b2a(xr)
				if (zr is None):
					if xr in vr.h:
						order.add(-1,xr,-1)
						vr.remove(xr)
						ct_vr = (ct_vr - 1)
					xr = (xr + 1)
					continue
			if (zl is not None):
				if (self.a2b(zl) is None):
					if xl in vl.h:
						order.add(xl,-1,zl)
						prev = zl
						vp.remove(zl)
						ct_vp = (ct_vp - 1)
						vl.remove(xl)
						ct_vl = (ct_vl - 1)
						xp = (zl + 1)
					xl = (xl + 1)
					continue
			if (zr is not None):
				if (ref.a2b(zr) is None):
					if xr in vr.h:
						order.add(-1,xr,zr)
						prev = zr
						vp.remove(zr)
						ct_vp = (ct_vp - 1)
						vr.remove(xr)
						ct_vr = (ct_vr - 1)
						xp = (zr + 1)
					xr = (xr + 1)
					continue
			if ((((zl is not None) and ((zr is not None))) and ((self.a2b(zl) is not None))) and ((ref.a2b(zr) is not None))):
				if ((zl == ((prev + 1))) or ((zr != ((prev + 1))))):
					if xr in vr.h:
						order.add(ref.a2b(zr),xr,zr)
						prev = zr
						vp.remove(zr)
						ct_vp = (ct_vp - 1)
						key = ref.a2b(zr)
						vl.remove(key)
						ct_vl = (ct_vl - 1)
						vr.remove(xr)
						ct_vr = (ct_vr - 1)
						xp = (zr + 1)
						xl = (ref.a2b(zr) + 1)
					xr = (xr + 1)
					continue
				else:
					if xl in vl.h:
						order.add(xl,self.a2b(zl),zl)
						prev = zl
						vp.remove(zl)
						ct_vp = (ct_vp - 1)
						vl.remove(xl)
						ct_vl = (ct_vl - 1)
						key1 = self.a2b(zl)
						vr.remove(key1)
						ct_vr = (ct_vr - 1)
						xp = (zl + 1)
						xr = (self.a2b(zl) + 1)
					xl = (xl + 1)
					continue
			xp = (xp + 1)
			xl = (xl + 1)
			xr = (xr + 1)
		return order

Alignment._hx_class = Alignment


class CellBuilder:
	_hx_class_name = "CellBuilder"
	_hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "links"]
CellBuilder._hx_class = CellBuilder


class CellInfo:
	_hx_class_name = "CellInfo"
	_hx_fields = ["raw", "value", "pretty_value", "category", "category_given_tr", "separator", "pretty_separator", "updated", "conflicted", "pvalue", "lvalue", "rvalue"]
	_hx_methods = ["toString"]

	def __init__(self):
		self.raw = None
		self.value = None
		self.pretty_value = None
		self.category = None
		self.category_given_tr = None
		self.separator = None
		self.pretty_separator = None
		self.updated = None
		self.conflicted = None
		self.pvalue = None
		self.lvalue = None
		self.rvalue = None

	def toString(self):
		if (not self.updated):
			return self.value
		if (not self.conflicted):
			return ((HxOverrides.stringOrNull(self.lvalue) + "::") + HxOverrides.stringOrNull(self.rvalue))
		return ((((HxOverrides.stringOrNull(self.pvalue) + "||") + HxOverrides.stringOrNull(self.lvalue)) + "::") + HxOverrides.stringOrNull(self.rvalue))

CellInfo._hx_class = CellInfo


class Class:
	_hx_class_name = "Class"
Class._hx_class = Class


class CompareFlags:
	_hx_class_name = "CompareFlags"
	_hx_fields = ["ordered", "show_unchanged", "unchanged_context", "always_show_order", "never_show_order", "show_unchanged_columns", "unchanged_column_context", "always_show_header", "acts", "ids", "columns_to_ignore", "allow_nested_cells"]
	_hx_methods = ["filter", "allowUpdate", "allowInsert", "allowDelete", "getIgnoredColumns", "addPrimaryKey", "ignoreColumn"]

	def __init__(self):
		self.ordered = None
		self.show_unchanged = None
		self.unchanged_context = None
		self.always_show_order = None
		self.never_show_order = None
		self.show_unchanged_columns = None
		self.unchanged_column_context = None
		self.always_show_header = None
		self.acts = None
		self.ids = None
		self.columns_to_ignore = None
		self.allow_nested_cells = None
		self.ordered = True
		self.show_unchanged = False
		self.unchanged_context = 1
		self.always_show_order = False
		self.never_show_order = True
		self.show_unchanged_columns = False
		self.unchanged_column_context = 1
		self.always_show_header = True
		self.acts = None
		self.ids = None
		self.columns_to_ignore = None
		self.allow_nested_cells = False

	def filter(self,act,allow):
		if (self.acts is None):
			self.acts = haxe_ds_StringMap()
			self.acts.h["update"] = (not allow)
			self.acts.h["insert"] = (not allow)
			self.acts.h["delete"] = (not allow)
		if (not act in self.acts.h):
			return False
		self.acts.h[act] = allow
		return True

	def allowUpdate(self):
		if (self.acts is None):
			return True
		return "update" in self.acts.h

	def allowInsert(self):
		if (self.acts is None):
			return True
		return "insert" in self.acts.h

	def allowDelete(self):
		if (self.acts is None):
			return True
		return "delete" in self.acts.h

	def getIgnoredColumns(self):
		if (self.columns_to_ignore is None):
			return None
		ignore = haxe_ds_StringMap()
		_g1 = 0
		_g = len(self.columns_to_ignore)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			ignore.h[(self.columns_to_ignore[i] if i >= 0 and i < len(self.columns_to_ignore) else None)] = True
		return ignore

	def addPrimaryKey(self,column):
		if (self.ids is None):
			self.ids = list()
		_this = self.ids
		_this.append(column)

	def ignoreColumn(self,column):
		if (self.columns_to_ignore is None):
			self.columns_to_ignore = list()
		_this = self.columns_to_ignore
		_this.append(column)

CompareFlags._hx_class = CompareFlags


class CompareTable:
	_hx_class_name = "CompareTable"
	_hx_fields = ["comp", "indexes"]
	_hx_methods = ["run", "align", "getComparisonState", "alignCore", "alignCore2", "alignColumns", "testHasSameColumns", "hasSameColumns2", "testIsEqual", "isEqual2", "compareCore", "storeIndexes", "getIndexes"]

	def __init__(self,comp):
		self.comp = None
		self.indexes = None
		self.comp = comp

	def run(self):
		more = self.compareCore()
		while (more and self.comp.run_to_completion):
			more = self.compareCore()
		return (not more)

	def align(self):
		while (not self.comp.completed):
			self.run()
		alignment = Alignment()
		self.alignCore(alignment)
		return alignment

	def getComparisonState(self):
		return self.comp

	def alignCore(self,align):
		if (self.comp.p is None):
			self.alignCore2(align,self.comp.a,self.comp.b)
			return
		align.reference = Alignment()
		self.alignCore2(align,self.comp.p,self.comp.b)
		self.alignCore2(align.reference,self.comp.p,self.comp.a)
		align.meta.reference = align.reference.meta

	def alignCore2(self,align,a,b):
		if (align.meta is None):
			align.meta = Alignment()
		self.alignColumns(align.meta,a,b)
		column_order = align.meta.toOrder()
		align.range(a.get_height(),b.get_height())
		align.tables(a,b)
		align.setRowlike(True)
		w = a.get_width()
		ha = a.get_height()
		hb = b.get_height()
		av = a.getCellView()
		ids = None
		ignore = None
		if (self.comp.compare_flags is not None):
			ids = self.comp.compare_flags.ids
			ignore = self.comp.compare_flags.getIgnoredColumns()
		common_units = list()
		ra_header = align.getSourceHeader()
		rb_header = align.getSourceHeader()
		_g = 0
		_g1 = column_order.getList()
		while (_g < len(_g1)):
			unit = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if (((unit.l >= 0) and ((unit.r >= 0))) and ((unit.p != -1))):
				if (ignore is not None):
					if (((unit.l >= 0) and ((ra_header >= 0))) and ((ra_header < a.get_height()))):
						name = av.toString(a.getCell(unit.l,ra_header))
						if name in ignore.h:
							continue
					if (((unit.r >= 0) and ((rb_header >= 0))) and ((rb_header < b.get_height()))):
						name1 = av.toString(b.getCell(unit.r,rb_header))
						if name1 in ignore.h:
							continue
				common_units.append(unit)
		if (ids is not None):
			index = IndexPair()
			ids_as_map = haxe_ds_StringMap()
			_g2 = 0
			while (_g2 < len(ids)):
				id = (ids[_g2] if _g2 >= 0 and _g2 < len(ids) else None)
				_g2 = (_g2 + 1)
				ids_as_map.h[id] = True
				True
			_g3 = 0
			while (_g3 < len(common_units)):
				unit1 = (common_units[_g3] if _g3 >= 0 and _g3 < len(common_units) else None)
				_g3 = (_g3 + 1)
				na = av.toString(a.getCell(unit1.l,0))
				nb = av.toString(b.getCell(unit1.r,0))
				if (na in ids_as_map.h or nb in ids_as_map.h):
					index.addColumns(unit1.l,unit1.r)
					align.addIndexColumns(unit1)
			index.indexTables(a,b,1)
			if (self.indexes is not None):
				_this = self.indexes
				_this.append(index)
			_g4 = 0
			while (_g4 < ha):
				j = _g4
				_g4 = (_g4 + 1)
				cross = index.queryLocal(j)
				spot_a = cross.spot_a
				spot_b = cross.spot_b
				if ((spot_a != 1) or ((spot_b != 1))):
					continue
				align.link(j,python_internal_ArrayImpl._get(cross.item_b.lst, 0))
		else:
			N = 5
			columns = list()
			if (len(common_units) > N):
				columns_eval = list()
				_g11 = 0
				_g5 = len(common_units)
				while (_g11 < _g5):
					i = _g11
					_g11 = (_g11 + 1)
					ct = 0
					mem = haxe_ds_StringMap()
					mem2 = haxe_ds_StringMap()
					ca = (common_units[i] if i >= 0 and i < len(common_units) else None).l
					cb = (common_units[i] if i >= 0 and i < len(common_units) else None).r
					_g21 = 0
					while (_g21 < ha):
						j1 = _g21
						_g21 = (_g21 + 1)
						key = av.toString(a.getCell(ca,j1))
						if (not key in mem.h):
							mem.h[key] = 1
							ct = (ct + 1)
					_g22 = 0
					while (_g22 < hb):
						j2 = _g22
						_g22 = (_g22 + 1)
						key1 = av.toString(b.getCell(cb,j2))
						if (not key1 in mem2.h):
							mem2.h[key1] = 1
							ct = (ct + 1)
					columns_eval.append([i, ct])
				def _hx_local_5(a1,b1):
					if ((a1[1] if 1 < len(a1) else None) < (b1[1] if 1 < len(b1) else None)):
						return 1
					if ((a1[1] if 1 < len(a1) else None) > (b1[1] if 1 < len(b1) else None)):
						return -1
					if ((a1[0] if 0 < len(a1) else None) > (b1[0] if 0 < len(b1) else None)):
						return 1
					if ((a1[0] if 0 < len(a1) else None) < (b1[0] if 0 < len(b1) else None)):
						return -1
					return 0
				sorter = _hx_local_5
				columns_eval.sort(key= python_lib_Functools.cmp_to_key(sorter))
				def _hx_local_6(v):
					return (v[0] if 0 < len(v) else None)
				columns = Lambda.array(Lambda.map(columns_eval,_hx_local_6))
				columns = columns[0:N]
			else:
				_g12 = 0
				_g6 = len(common_units)
				while (_g12 < _g6):
					i1 = _g12
					_g12 = (_g12 + 1)
					columns.append(i1)
			top = None
			v1 = Math.pow(2,len(columns))
			top = Math.floor((v1 + 0.5))
			pending = haxe_ds_IntMap()
			_g7 = 0
			while (_g7 < ha):
				j3 = _g7
				_g7 = (_g7 + 1)
				pending.set(j3,j3)
			pending_ct = ha
			added_columns = haxe_ds_IntMap()
			index_ct = 0
			index_top = None
			_g8 = 0
			while (_g8 < top):
				k = _g8
				_g8 = (_g8 + 1)
				if (k == 0):
					continue
				if (pending_ct == 0):
					break
				active_columns = list()
				kk = k
				at = 0
				while (kk > 0):
					if ((kk % 2) == 1):
						active_columns.append((columns[at] if at >= 0 and at < len(columns) else None))
					kk = (kk >> 1)
					at = (at + 1)
				index1 = IndexPair()
				_g23 = 0
				_g13 = len(active_columns)
				while (_g23 < _g13):
					k1 = _g23
					_g23 = (_g23 + 1)
					col = (active_columns[k1] if k1 >= 0 and k1 < len(active_columns) else None)
					unit2 = (common_units[col] if col >= 0 and col < len(common_units) else None)
					index1.addColumns(unit2.l,unit2.r)
					if (not col in added_columns.h):
						align.addIndexColumns(unit2)
						added_columns.set(col,True)
				index1.indexTables(a,b,1)
				if (k == ((top - 1))):
					index_top = index1
				h = a.get_height()
				if (b.get_height() > h):
					h = b.get_height()
				if (h < 1):
					h = 1
				wide_top_freq = index1.getTopFreq()
				ratio = wide_top_freq
				ratio = (ratio / ((h + 20)))
				if (ratio >= 0.1):
					if ((index_ct > 0) or ((k < ((top - 1))))):
						continue
				index_ct = (index_ct + 1)
				if (self.indexes is not None):
					_this1 = self.indexes
					_this1.append(index1)
				fixed = list()
				_hx_local_11 = pending.keys()
				while _hx_local_11.hasNext():
					j4 = _hx_local_11.next()
					cross1 = index1.queryLocal(j4)
					spot_a1 = cross1.spot_a
					spot_b1 = cross1.spot_b
					if ((spot_a1 != 1) or ((spot_b1 != 1))):
						continue
					fixed.append(j4)
					align.link(j4,python_internal_ArrayImpl._get(cross1.item_b.lst, 0))
				_g24 = 0
				_g14 = len(fixed)
				while (_g24 < _g14):
					j5 = _g24
					_g24 = (_g24 + 1)
					pending.remove((fixed[j5] if j5 >= 0 and j5 < len(fixed) else None))
					pending_ct = (pending_ct - 1)
			if (index_top is not None):
				offset = 0
				scale = 1
				_g9 = 0
				while (_g9 < 2):
					sgn = _g9
					_g9 = (_g9 + 1)
					if (pending_ct > 0):
						xb = None
						if ((scale == -1) and ((hb > 0))):
							xb = (hb - 1)
						_g15 = 0
						while (_g15 < ha):
							xa0 = _g15
							_g15 = (_g15 + 1)
							xa = ((xa0 * scale) + offset)
							xb2 = align.a2b(xa)
							if (xb2 is not None):
								xb = (xb2 + scale)
								if ((xb >= hb) or ((xb < 0))):
									break
								continue
							if (xb is None):
								continue
							ka = index_top.localKey(xa)
							kb = index_top.remoteKey(xb)
							if (ka != kb):
								continue
							align.link(xa,xb)
							pending_ct = (pending_ct - 1)
							xb = (xb + scale)
							if ((xb >= hb) or ((xb < 0))):
								break
							if (pending_ct == 0):
								break
					offset = (ha - 1)
					scale = -1
		if ((ha > 0) and ((hb > 0))):
			align.link(0,0)

	def alignColumns(self,align,a,b):
		align.range(a.get_width(),b.get_width())
		align.tables(a,b)
		align.setRowlike(False)
		slop = 5
		va = a.getCellView()
		vb = b.getCellView()
		ra_best = 0
		rb_best = 0
		ct_best = -1
		ma_best = None
		mb_best = None
		ra_header = 0
		rb_header = 0
		ra_uniques = 0
		rb_uniques = 0
		_g = 0
		while (_g < slop):
			ra = _g
			_g = (_g + 1)
			if (ra >= a.get_height()):
				break
			_g1 = 0
			while (_g1 < slop):
				rb = _g1
				_g1 = (_g1 + 1)
				if (rb >= b.get_height()):
					break
				ma = haxe_ds_StringMap()
				mb = haxe_ds_StringMap()
				ct = 0
				uniques = 0
				_g3 = 0
				_g2 = a.get_width()
				while (_g3 < _g2):
					ca = _g3
					_g3 = (_g3 + 1)
					key = va.toString(a.getCell(ca,ra))
					if key in ma.h:
						ma.h[key] = -1
						uniques = (uniques - 1)
					else:
						ma.h[key] = ca
						uniques = (uniques + 1)
				if (uniques > ra_uniques):
					ra_header = ra
					ra_uniques = uniques
				uniques = 0
				_g31 = 0
				_g21 = b.get_width()
				while (_g31 < _g21):
					cb = _g31
					_g31 = (_g31 + 1)
					key1 = vb.toString(b.getCell(cb,rb))
					if key1 in mb.h:
						mb.h[key1] = -1
						uniques = (uniques - 1)
					else:
						mb.h[key1] = cb
						uniques = (uniques + 1)
				if (uniques > rb_uniques):
					rb_header = rb
					rb_uniques = uniques
				_hx_local_5 = ma.keys()
				while _hx_local_5.hasNext():
					key2 = _hx_local_5.next()
					i0 = ma.h.get(key2,None)
					i1 = mb.h.get(key2,None)
					if (i1 is not None):
						if ((i1 >= 0) and ((i0 >= 0))):
							ct = (ct + 1)
				if (ct > ct_best):
					ct_best = ct
					ma_best = ma
					mb_best = mb
					ra_best = ra
					rb_best = rb
		if (ma_best is None):
			if ((a.get_height() > 0) and ((b.get_height() == 0))):
				align.headers(0,-1)
			elif ((a.get_height() == 0) and ((b.get_height() > 0))):
				align.headers(-1,0)
			return
		_hx_local_6 = ma_best.keys()
		while _hx_local_6.hasNext():
			key3 = _hx_local_6.next()
			i01 = ma_best.h.get(key3,None)
			i11 = mb_best.h.get(key3,None)
			if ((i11 is not None) and ((i01 is not None))):
				align.link(i01,i11)
		align.headers(ra_header,rb_header)

	def testHasSameColumns(self):
		p = self.comp.p
		a = self.comp.a
		b = self.comp.b
		eq = self.hasSameColumns2(a,b)
		if (eq and ((p is not None))):
			eq = self.hasSameColumns2(p,a)
		self.comp.has_same_columns = eq
		self.comp.has_same_columns_known = True
		return True

	def hasSameColumns2(self,a,b):
		if (a.get_width() != b.get_width()):
			return False
		if ((a.get_height() == 0) or ((b.get_height() == 0))):
			return True
		av = a.getCellView()
		_g1 = 0
		_g = a.get_width()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_g3 = (i + 1)
			_g2 = a.get_width()
			while (_g3 < _g2):
				j = _g3
				_g3 = (_g3 + 1)
				if av.equals(a.getCell(i,0),a.getCell(j,0)):
					return False
			if (not av.equals(a.getCell(i,0),b.getCell(i,0))):
				return False
		return True

	def testIsEqual(self):
		p = self.comp.p
		a = self.comp.a
		b = self.comp.b
		eq = self.isEqual2(a,b)
		if (eq and ((p is not None))):
			eq = self.isEqual2(p,a)
		self.comp.is_equal = eq
		self.comp.is_equal_known = True
		return True

	def isEqual2(self,a,b):
		if ((a.get_width() != b.get_width()) or ((a.get_height() != b.get_height()))):
			return False
		av = a.getCellView()
		_g1 = 0
		_g = a.get_height()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_g3 = 0
			_g2 = a.get_width()
			while (_g3 < _g2):
				j = _g3
				_g3 = (_g3 + 1)
				if (not av.equals(a.getCell(j,i),b.getCell(j,i))):
					return False
		return True

	def compareCore(self):
		if self.comp.completed:
			return False
		if (not self.comp.is_equal_known):
			return self.testIsEqual()
		if (not self.comp.has_same_columns_known):
			return self.testHasSameColumns()
		self.comp.completed = True
		return False

	def storeIndexes(self):
		self.indexes = list()

	def getIndexes(self):
		return self.indexes

CompareTable._hx_class = CompareTable


class Coopy:
	_hx_class_name = "Coopy"
	_hx_fields = ["format_preference", "delim_preference", "extern_preference", "output_format", "nested_output", "order_set", "order_preference", "io", "mv", "status", "daff_cmd"]
	_hx_methods = ["checkFormat", "setFormat", "saveTable", "saveText", "loadTable", "command", "installGitDriver", "coopyhx"]
	_hx_statics = ["VERSION", "compareTables", "compareTables3", "keepAround", "cellFor", "jsonToTable", "main", "show", "jsonify"]

	def __init__(self):
		self.format_preference = None
		self.delim_preference = None
		self.extern_preference = None
		self.output_format = None
		self.nested_output = None
		self.order_set = None
		self.order_preference = None
		self.io = None
		self.mv = None
		self.status = None
		self.daff_cmd = None
		self.extern_preference = False
		self.format_preference = None
		self.delim_preference = None
		self.output_format = "copy"
		self.nested_output = False
		self.order_set = False
		self.order_preference = False

	def checkFormat(self,name):
		if self.extern_preference:
			return self.format_preference
		ext = ""
		pt = name.rfind(".", 0, len(name))
		if (pt >= 0):
			_this = HxString.substr(name,(pt + 1),None)
			ext = _this.lower()
			_hx_local_0 = len(ext)
			if (_hx_local_0 == 4):
				if (ext == "json"):
					self.format_preference = "json"
				else:
					ext = ""
			elif (_hx_local_0 == 7):
				if (ext == "sqlite3"):
					self.format_preference = "sqlite"
				else:
					ext = ""
			elif (_hx_local_0 == 6):
				if (ext == "ndjson"):
					self.format_preference = "ndjson"
				elif (ext == "sqlite"):
					self.format_preference = "sqlite"
				else:
					ext = ""
			elif (_hx_local_0 == 3):
				if (ext == "csv"):
					self.format_preference = "csv"
					self.delim_preference = ","
				elif (ext == "tsv"):
					self.format_preference = "csv"
					self.delim_preference = "\t"
				elif (ext == "ssv"):
					self.format_preference = "csv"
					self.delim_preference = ";"
				else:
					ext = ""
			else:
				ext = ""
		self.nested_output = ((self.format_preference == "json") or ((self.format_preference == "ndjson")))
		self.order_preference = (not self.nested_output)
		return ext

	def setFormat(self,name):
		self.extern_preference = False
		self.checkFormat(("." + ("null" if name is None else name)))
		self.extern_preference = True

	def saveTable(self,name,t):
		if (self.output_format != "copy"):
			self.setFormat(self.output_format)
		txt = ""
		self.checkFormat(name)
		if (self.format_preference == "csv"):
			csv = Csv(self.delim_preference)
			txt = csv.renderTable(t)
		elif (self.format_preference == "ndjson"):
			txt = Ndjson(t).render()
		elif (self.format_preference == "sqlite"):
			self.io.writeStderr("! Cannot yet output to sqlite, aborting\n")
			return False
		else:
			value = Coopy.jsonify(t)
			txt = haxe_format_JsonPrinter.print(value,None,"  ")
		return self.saveText(name,txt)

	def saveText(self,name,txt):
		if (name != "-"):
			self.io.saveContent(name,txt)
		else:
			self.io.writeStdout(txt)
		return True

	def loadTable(self,name):
		txt = self.io.getContent(name)
		ext = self.checkFormat(name)
		if (ext == "sqlite"):
			sql = self.io.openSqliteDatabase(name)
			if (sql is None):
				self.io.writeStderr("! Cannot open database, aborting\n")
				return None
			helper = SqliteHelper()
			names = helper.getTableNames(sql)
			if (names is None):
				self.io.writeStderr("! Cannot find database tables, aborting\n")
				return None
			if (len(names) == 0):
				self.io.writeStderr("! No tables in database, aborting\n")
				return None
			tab = SqlTable(sql, SqlTableName((names[0] if 0 < len(names) else None)), helper)
			return tab
		if (ext == "ndjson"):
			t = SimpleTable(0, 0)
			ndjson = Ndjson(t)
			ndjson.parse(txt)
			return t
		if ((ext == "json") or ((ext == ""))):
			try:
				json = python_lib_Json.loads(txt,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
				self.format_preference = "json"
				t1 = Coopy.jsonToTable(json)
				if (t1 is None):
					raise _HxException("JSON failed")
				return t1
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				if (ext == "json"):
					raise _HxException(e)
		self.format_preference = "csv"
		csv = Csv(self.delim_preference)
		output = SimpleTable(0, 0)
		csv.parseTable(txt,output)
		if (output is not None):
			output.trimBlank()
		return output

	def command(self,io,cmd,args):
		r = 0
		if io.async():
			r = io.command(cmd,args)
		if (r != 999):
			io.writeStdout(("$ " + ("null" if cmd is None else cmd)))
			_g = 0
			while (_g < len(args)):
				arg = (args[_g] if _g >= 0 and _g < len(args) else None)
				_g = (_g + 1)
				io.writeStdout(" ")
				spaced = (arg.find(" ") >= 0)
				if spaced:
					io.writeStdout("\"")
				io.writeStdout(arg)
				if spaced:
					io.writeStdout("\"")
			io.writeStdout("\n")
		if (not io.async()):
			r = io.command(cmd,args)
		return r

	def installGitDriver(self,io,formats):
		r = 0
		if (self.status is None):
			self.status = haxe_ds_StringMap()
			self.daff_cmd = ""
		key = "hello"
		if (not key in self.status.h):
			io.writeStdout("Setting up git to use daff on")
			_g = 0
			while (_g < len(formats)):
				format = (formats[_g] if _g >= 0 and _g < len(formats) else None)
				_g = (_g + 1)
				io.writeStdout((" *." + ("null" if format is None else format)))
			io.writeStdout(" files\n")
			self.status.h[key] = r
		key = "can_run_git"
		if (not key in self.status.h):
			r = self.command(io,"git",["--version"])
			if (r == 999):
				return r
			self.status.h[key] = r
			if (r != 0):
				io.writeStderr("! Cannot run git, aborting\n")
				return 1
			io.writeStdout("- Can run git\n")
		daffs = ["daff", "daff.rb", "daff.py"]
		if (self.daff_cmd == ""):
			_g1 = 0
			while (_g1 < len(daffs)):
				daff = (daffs[_g1] if _g1 >= 0 and _g1 < len(daffs) else None)
				_g1 = (_g1 + 1)
				key1 = ("can_run_" + ("null" if daff is None else daff))
				if (not key1 in self.status.h):
					r = self.command(io,daff,["version"])
					if (r == 999):
						return r
					self.status.h[key1] = r
					if (r == 0):
						self.daff_cmd = daff
						io.writeStdout((((("- Can run " + ("null" if daff is None else daff)) + " as \"") + ("null" if daff is None else daff)) + "\"\n"))
						break
			if (self.daff_cmd == ""):
				io.writeStderr("! Cannot find daff, is it in your path?\n")
				return 1
		_g2 = 0
		while (_g2 < len(formats)):
			format1 = (formats[_g2] if _g2 >= 0 and _g2 < len(formats) else None)
			_g2 = (_g2 + 1)
			key = ("have_diff_driver_" + ("null" if format1 is None else format1))
			if (not key in self.status.h):
				r = self.command(io,"git",["config", "--global", "--get", (("diff.daff-" + ("null" if format1 is None else format1)) + ".command")])
				if (r == 999):
					return r
				self.status.h[key] = r
			have_diff_driver = (self.status.h.get(key,None) == 0)
			key = ("add_diff_driver_" + ("null" if format1 is None else format1))
			if (not key in self.status.h):
				if (not have_diff_driver):
					r = self.command(io,"git",["config", "--global", (("diff.daff-" + ("null" if format1 is None else format1)) + ".command"), (HxOverrides.stringOrNull(self.daff_cmd) + " diff --color --git")])
					if (r == 999):
						return r
					io.writeStdout((("- Added diff driver for " + ("null" if format1 is None else format1)) + "\n"))
				else:
					r = 0
					io.writeStdout((("- Already have diff driver for " + ("null" if format1 is None else format1)) + ", not touching it\n"))
				self.status.h[key] = r
			key = ("have_merge_driver_" + ("null" if format1 is None else format1))
			if (not key in self.status.h):
				r = self.command(io,"git",["config", "--global", "--get", (("merge.daff-" + ("null" if format1 is None else format1)) + ".driver")])
				if (r == 999):
					return r
				self.status.h[key] = r
			have_merge_driver = (self.status.h.get(key,None) == 0)
			key = ("name_merge_driver_" + ("null" if format1 is None else format1))
			if (not key in self.status.h):
				if (not have_merge_driver):
					r = self.command(io,"git",["config", "--global", (("merge.daff-" + ("null" if format1 is None else format1)) + ".name"), (("daff tabular " + ("null" if format1 is None else format1)) + " merge")])
					if (r == 999):
						return r
				else:
					r = 0
				self.status.h[key] = r
			key = ("add_merge_driver_" + ("null" if format1 is None else format1))
			if (not key in self.status.h):
				if (not have_merge_driver):
					r = self.command(io,"git",["config", "--global", (("merge.daff-" + ("null" if format1 is None else format1)) + ".driver"), (HxOverrides.stringOrNull(self.daff_cmd) + " merge --output %A %O %A %B")])
					if (r == 999):
						return r
					io.writeStdout((("- Added merge driver for " + ("null" if format1 is None else format1)) + "\n"))
				else:
					r = 0
					io.writeStdout((("- Already have merge driver for " + ("null" if format1 is None else format1)) + ", not touching it\n"))
				self.status.h[key] = r
		if (not io.exists(".git/config")):
			io.writeStderr("! This next part needs to happen in a git repository.\n")
			io.writeStderr("! Please run again from the root of a git repository.\n")
			return 1
		attr = ".gitattributes"
		txt = ""
		post = ""
		if (not io.exists(attr)):
			io.writeStdout("- No .gitattributes file\n")
		else:
			io.writeStdout("- You have a .gitattributes file\n")
			txt = io.getContent(attr)
		need_update = False
		_g3 = 0
		while (_g3 < len(formats)):
			format2 = (formats[_g3] if _g3 >= 0 and _g3 < len(formats) else None)
			_g3 = (_g3 + 1)
			def _hx_local_4():
				_hx_str = ("*." + ("null" if format2 is None else format2))
				return txt.find(_hx_str)
			if (_hx_local_4() >= 0):
				io.writeStderr((("- Your .gitattributes file already mentions *." + ("null" if format2 is None else format2)) + "\n"))
			else:
				post = (("null" if post is None else post) + HxOverrides.stringOrNull(((((("*." + ("null" if format2 is None else format2)) + " diff=daff-") + ("null" if format2 is None else format2)) + "\n"))))
				post = (("null" if post is None else post) + HxOverrides.stringOrNull(((((("*." + ("null" if format2 is None else format2)) + " merge=daff-") + ("null" if format2 is None else format2)) + "\n"))))
				io.writeStdout("- Placing the following lines in .gitattributes:\n")
				io.writeStdout(post)
				if ((txt != "") and (not need_update)):
					txt = (("null" if txt is None else txt) + "\n")
				txt = (("null" if txt is None else txt) + ("null" if post is None else post))
				need_update = True
		if need_update:
			io.saveContent(attr,txt)
		io.writeStdout("- Done!\n")
		return 0

	def coopyhx(self,io):
		args = io.args()
		if ((args[0] if 0 < len(args) else None) == "--keep"):
			return Coopy.keepAround()
		more = True
		output = None
		css_output = None
		fragment = False
		pretty = True
		inplace = False
		git = False
		color = False
		flags = CompareFlags()
		flags.always_show_header = True
		while more:
			more = False
			_g1 = 0
			_g = len(args)
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				tag = (args[i] if i >= 0 and i < len(args) else None)
				if (tag == "--output"):
					more = True
					output = python_internal_ArrayImpl._get(args, (i + 1))
					pos = i
					if (pos < 0):
						pos = (len(args) + pos)
					if (pos < 0):
						pos = 0
					res = args[pos:(pos + 2)]
					del args[pos:(pos + 2)]
					res
					break
				elif (tag == "--css"):
					more = True
					fragment = True
					css_output = python_internal_ArrayImpl._get(args, (i + 1))
					pos1 = i
					if (pos1 < 0):
						pos1 = (len(args) + pos1)
					if (pos1 < 0):
						pos1 = 0
					res1 = args[pos1:(pos1 + 2)]
					del args[pos1:(pos1 + 2)]
					res1
					break
				elif (tag == "--fragment"):
					more = True
					fragment = True
					pos2 = i
					if (pos2 < 0):
						pos2 = (len(args) + pos2)
					if (pos2 < 0):
						pos2 = 0
					res2 = args[pos2:(pos2 + 1)]
					del args[pos2:(pos2 + 1)]
					res2
					break
				elif (tag == "--plain"):
					more = True
					pretty = False
					pos3 = i
					if (pos3 < 0):
						pos3 = (len(args) + pos3)
					if (pos3 < 0):
						pos3 = 0
					res3 = args[pos3:(pos3 + 1)]
					del args[pos3:(pos3 + 1)]
					res3
					break
				elif (tag == "--all"):
					more = True
					flags.show_unchanged = True
					pos4 = i
					if (pos4 < 0):
						pos4 = (len(args) + pos4)
					if (pos4 < 0):
						pos4 = 0
					res4 = args[pos4:(pos4 + 1)]
					del args[pos4:(pos4 + 1)]
					res4
					break
				elif (tag == "--act"):
					more = True
					if (flags.acts is None):
						flags.acts = haxe_ds_StringMap()
					flags.acts.h[python_internal_ArrayImpl._get(args, (i + 1))] = True
					True
					pos5 = i
					if (pos5 < 0):
						pos5 = (len(args) + pos5)
					if (pos5 < 0):
						pos5 = 0
					res5 = args[pos5:(pos5 + 2)]
					del args[pos5:(pos5 + 2)]
					res5
					break
				elif (tag == "--context"):
					more = True
					context = Std.parseInt(python_internal_ArrayImpl._get(args, (i + 1)))
					if (context >= 0):
						flags.unchanged_context = context
					pos6 = i
					if (pos6 < 0):
						pos6 = (len(args) + pos6)
					if (pos6 < 0):
						pos6 = 0
					res6 = args[pos6:(pos6 + 2)]
					del args[pos6:(pos6 + 2)]
					res6
					break
				elif (tag == "--inplace"):
					more = True
					inplace = True
					pos7 = i
					if (pos7 < 0):
						pos7 = (len(args) + pos7)
					if (pos7 < 0):
						pos7 = 0
					res7 = args[pos7:(pos7 + 1)]
					del args[pos7:(pos7 + 1)]
					res7
					break
				elif (tag == "--git"):
					more = True
					git = True
					pos8 = i
					if (pos8 < 0):
						pos8 = (len(args) + pos8)
					if (pos8 < 0):
						pos8 = 0
					res8 = args[pos8:(pos8 + 1)]
					del args[pos8:(pos8 + 1)]
					res8
					break
				elif (tag == "--unordered"):
					more = True
					flags.ordered = False
					flags.unchanged_context = 0
					self.order_set = True
					pos9 = i
					if (pos9 < 0):
						pos9 = (len(args) + pos9)
					if (pos9 < 0):
						pos9 = 0
					res9 = args[pos9:(pos9 + 1)]
					del args[pos9:(pos9 + 1)]
					res9
					break
				elif (tag == "--ordered"):
					more = True
					flags.ordered = True
					self.order_set = True
					pos10 = i
					if (pos10 < 0):
						pos10 = (len(args) + pos10)
					if (pos10 < 0):
						pos10 = 0
					res10 = args[pos10:(pos10 + 1)]
					del args[pos10:(pos10 + 1)]
					res10
					break
				elif (tag == "--color"):
					more = True
					color = True
					pos11 = i
					if (pos11 < 0):
						pos11 = (len(args) + pos11)
					if (pos11 < 0):
						pos11 = 0
					res11 = args[pos11:(pos11 + 1)]
					del args[pos11:(pos11 + 1)]
					res11
					break
				elif (tag == "--input-format"):
					more = True
					self.setFormat(python_internal_ArrayImpl._get(args, (i + 1)))
					pos12 = i
					if (pos12 < 0):
						pos12 = (len(args) + pos12)
					if (pos12 < 0):
						pos12 = 0
					res12 = args[pos12:(pos12 + 2)]
					del args[pos12:(pos12 + 2)]
					res12
					break
				elif (tag == "--output-format"):
					more = True
					self.output_format = python_internal_ArrayImpl._get(args, (i + 1))
					pos13 = i
					if (pos13 < 0):
						pos13 = (len(args) + pos13)
					if (pos13 < 0):
						pos13 = 0
					res13 = args[pos13:(pos13 + 2)]
					del args[pos13:(pos13 + 2)]
					res13
					break
				elif (tag == "--id"):
					more = True
					if (flags.ids is None):
						flags.ids = list()
					_this = flags.ids
					_this.append(python_internal_ArrayImpl._get(args, (i + 1)))
					pos14 = i
					if (pos14 < 0):
						pos14 = (len(args) + pos14)
					if (pos14 < 0):
						pos14 = 0
					res14 = args[pos14:(pos14 + 2)]
					del args[pos14:(pos14 + 2)]
					res14
					break
				elif (tag == "--ignore"):
					more = True
					if (flags.columns_to_ignore is None):
						flags.columns_to_ignore = list()
					_this1 = flags.columns_to_ignore
					_this1.append(python_internal_ArrayImpl._get(args, (i + 1)))
					pos15 = i
					if (pos15 < 0):
						pos15 = (len(args) + pos15)
					if (pos15 < 0):
						pos15 = 0
					res15 = args[pos15:(pos15 + 2)]
					del args[pos15:(pos15 + 2)]
					res15
					break
				elif (tag == "--index"):
					more = True
					flags.always_show_order = True
					flags.never_show_order = False
					pos16 = i
					if (pos16 < 0):
						pos16 = (len(args) + pos16)
					if (pos16 < 0):
						pos16 = 0
					res16 = args[pos16:(pos16 + 1)]
					del args[pos16:(pos16 + 1)]
					res16
					break
		cmd = (args[0] if 0 < len(args) else None)
		if (len(args) < 2):
			if (cmd == "version"):
				io.writeStdout((HxOverrides.stringOrNull(Coopy.VERSION) + "\n"))
				return 0
			if (cmd == "git"):
				io.writeStdout("You can use daff to improve git's handling of csv files, by using it as a\ndiff driver (for showing what has changed) and as a merge driver (for merging\nchanges between multiple versions).\n")
				io.writeStdout("\n")
				io.writeStdout("Automatic setup\n")
				io.writeStdout("---------------\n\n")
				io.writeStdout("Run:\n")
				io.writeStdout("  daff git csv\n")
				io.writeStdout("\n")
				io.writeStdout("Manual setup\n")
				io.writeStdout("------------\n\n")
				io.writeStdout("Create and add a file called .gitattributes in the root directory of your\nrepository, containing:\n\n")
				io.writeStdout("  *.csv diff=daff-csv\n")
				io.writeStdout("  *.csv merge=daff-csv\n")
				io.writeStdout("\nCreate a file called .gitconfig in your home directory (or alternatively\nopen .git/config for a particular repository) and add:\n\n")
				io.writeStdout("  [diff \"daff-csv\"]\n")
				io.writeStdout("  command = daff diff --color --git\n")
				io.writeStderr("\n")
				io.writeStdout("  [merge \"daff-csv\"]\n")
				io.writeStdout("  name = daff tabular merge\n")
				io.writeStdout("  driver = daff merge --output %A %O %A %B\n\n")
				io.writeStderr("Make sure you can run daff from the command-line as just \"daff\" - if not,\nreplace \"daff\" in the driver and command lines above with the correct way\nto call it. Omit --color if your terminal does not support ANSI colors.")
				io.writeStderr("\n")
				return 0
			io.writeStderr("daff can produce and apply tabular diffs.\n")
			io.writeStderr("Call as:\n")
			io.writeStderr("  daff [--color] [--output OUTPUT.csv] a.csv b.csv\n")
			io.writeStderr("  daff [--output OUTPUT.csv] parent.csv a.csv b.csv\n")
			io.writeStderr("  daff [--output OUTPUT.ndjson] a.ndjson b.ndjson\n")
			io.writeStderr("  daff patch [--inplace] [--output OUTPUT.csv] a.csv patch.csv\n")
			io.writeStderr("  daff merge [--inplace] [--output OUTPUT.csv] parent.csv a.csv b.csv\n")
			io.writeStderr("  daff trim [--output OUTPUT.csv] source.csv\n")
			io.writeStderr("  daff render [--output OUTPUT.html] diff.csv\n")
			io.writeStderr("  daff copy in.csv out.tsv\n")
			io.writeStderr("  daff git\n")
			io.writeStderr("  daff version\n")
			io.writeStderr("\n")
			io.writeStderr("The --inplace option to patch and merge will result in modification of a.csv.\n")
			io.writeStderr("\n")
			io.writeStderr("If you need more control, here is the full list of flags:\n")
			io.writeStderr("  daff diff [--output OUTPUT.csv] [--context NUM] [--all] [--act ACT] a.csv b.csv\n")
			io.writeStderr("     --act ACT:     show only a certain kind of change (update, insert, delete)\n")
			io.writeStderr("     --all:         do not prune unchanged rows\n")
			io.writeStderr("     --color:       highlight changes with terminal colors\n")
			io.writeStderr("     --context NUM: show NUM rows of context\n")
			io.writeStderr("     --id:          specify column to use as primary key (repeat for multi-column key)\n")
			io.writeStderr("     --ignore:      specify column to ignore completely (can repeat)\n")
			io.writeStderr("     --input-format [csv|tsv|ssv|json]: set format to expect for input\n")
			io.writeStderr("     --ordered:     assume row order is meaningful (default for CSV)\n")
			io.writeStderr("     --output-format [csv|tsv|ssv|json|copy]: set format for output\n")
			io.writeStderr("     --unordered:   assume row order is meaningless (default for json formats)\n")
			io.writeStderr("\n")
			io.writeStderr("  daff diff --git path old-file old-hex old-mode new-file new-hex new-mode\n")
			io.writeStderr("     --git:         process arguments provided by git to diff drivers\n")
			io.writeStderr("     --index:       include row/columns numbers from orginal tables\n")
			io.writeStderr("\n")
			io.writeStderr("  daff render [--output OUTPUT.html] [--css CSS.css] [--fragment] [--plain] diff.csv\n")
			io.writeStderr("     --css CSS.css: generate a suitable css file to go with the html\n")
			io.writeStderr("     --fragment:    generate just a html fragment rather than a page\n")
			io.writeStderr("     --plain:       do not use fancy utf8 characters to make arrows prettier\n")
			return 1
		cmd1 = (args[0] if 0 < len(args) else None)
		offset = 1
		if (not Lambda.has(["diff", "patch", "merge", "trim", "render", "git", "version", "copy"],cmd1)):
			if ((cmd1.find(".") != -1) or ((cmd1.find("--") == 0))):
				cmd1 = "diff"
				offset = 0
		if (cmd1 == "git"):
			types = None
			_hx_len = (len(args) - offset)
			pos17 = offset
			if (pos17 < 0):
				pos17 = (len(args) + pos17)
			if (pos17 < 0):
				pos17 = 0
			res17 = args[pos17:(pos17 + _hx_len)]
			del args[pos17:(pos17 + _hx_len)]
			types = res17
			return self.installGitDriver(io,types)
		if git:
			ct = (len(args) - offset)
			if (ct != 7):
				io.writeStderr((("Expected 7 parameters from git, but got " + Std.string(ct)) + "\n"))
				return 1
			git_args = None
			pos18 = offset
			if (pos18 < 0):
				pos18 = (len(args) + pos18)
			if (pos18 < 0):
				pos18 = 0
			res18 = args[pos18:(pos18 + ct)]
			del args[pos18:(pos18 + ct)]
			git_args = res18
			len1 = len(args)
			pos19 = 0
			if (pos19 < 0):
				pos19 = (len(args) + pos19)
			if (pos19 < 0):
				pos19 = 0
			res19 = args[pos19:(pos19 + len1)]
			del args[pos19:(pos19 + len1)]
			res19
			offset = 0
			path = (git_args[0] if 0 < len(git_args) else None)
			old_file = (git_args[1] if 1 < len(git_args) else None)
			new_file = (git_args[4] if 4 < len(git_args) else None)
			io.writeStdout((("--- a/" + ("null" if path is None else path)) + "\n"))
			io.writeStdout((("+++ b/" + ("null" if path is None else path)) + "\n"))
			args.append(old_file)
			args.append(new_file)
		tool = self
		tool.io = io
		parent = None
		if ((len(args) - offset) >= 3):
			parent = tool.loadTable((args[offset] if offset >= 0 and offset < len(args) else None))
			offset = (offset + 1)
		aname = (args[offset] if offset >= 0 and offset < len(args) else None)
		a = tool.loadTable(aname)
		b = None
		if ((len(args) - offset) >= 2):
			if (cmd1 != "copy"):
				b = tool.loadTable(python_internal_ArrayImpl._get(args, (1 + offset)))
			else:
				output = python_internal_ArrayImpl._get(args, (1 + offset))
		if inplace:
			if (output is not None):
				io.writeStderr("Please do not use --inplace when specifying an output.\n")
			output = aname
			return 1
		if (output is None):
			output = "-"
		ok = True
		if (cmd1 == "diff"):
			if (not self.order_set):
				flags.ordered = self.order_preference
				if (not flags.ordered):
					flags.unchanged_context = 0
			flags.allow_nested_cells = self.nested_output
			ct1 = Coopy.compareTables3(parent,a,b,flags)
			align = ct1.align()
			td = TableDiff(align, flags)
			o = SimpleTable(0, 0)
			td.hilite(o)
			if color:
				render = TerminalDiffRender()
				tool.saveText(output,render.render(o))
			else:
				tool.saveTable(output,o)
		elif (cmd1 == "patch"):
			patcher = HighlightPatch(a, b)
			patcher.apply()
			tool.saveTable(output,a)
		elif (cmd1 == "merge"):
			merger = Merger(parent, a, b, flags)
			conflicts = merger.apply()
			ok = (conflicts == 0)
			if (conflicts > 0):
				io.writeStderr((((Std.string(conflicts) + " conflict") + HxOverrides.stringOrNull((("s" if ((conflicts > 1)) else "")))) + "\n"))
			tool.saveTable(output,a)
		elif (cmd1 == "trim"):
			tool.saveTable(output,a)
		elif (cmd1 == "render"):
			renderer = DiffRender()
			renderer.usePrettyArrows(pretty)
			renderer.render(a)
			if (not fragment):
				renderer.completeHtml()
			tool.saveText(output,renderer.html())
			if (css_output is not None):
				tool.saveText(css_output,renderer.sampleCss())
		elif (cmd1 == "copy"):
			tool.saveTable(output,a)
		if ok:
			return 0
		else:
			return 1

	@staticmethod
	def compareTables(local,remote,flags = None):
		comp = TableComparisonState()
		comp.a = local
		comp.b = remote
		comp.compare_flags = flags
		ct = CompareTable(comp)
		return ct

	@staticmethod
	def compareTables3(parent,local,remote,flags = None):
		comp = TableComparisonState()
		comp.p = parent
		comp.a = local
		comp.b = remote
		comp.compare_flags = flags
		ct = CompareTable(comp)
		return ct

	@staticmethod
	def keepAround():
		st = SimpleTable(1, 1)
		v = Viterbi()
		td = TableDiff(None, None)
		idx = Index()
		dr = DiffRender()
		cf = CompareFlags()
		hp = HighlightPatch(None, None)
		csv = Csv()
		tm = TableModifier(None)
		sc = SqlCompare(None, None, None)
		return 0

	@staticmethod
	def cellFor(x):
		return x

	@staticmethod
	def jsonToTable(json):
		output = None
		_g = 0
		_g1 = python_Boot.fields(json)
		while (_g < len(_g1)):
			name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			t = Reflect.field(json,name)
			columns = Reflect.field(t,"columns")
			if (columns is None):
				continue
			rows = Reflect.field(t,"rows")
			if (rows is None):
				continue
			output = SimpleTable(len(columns), len(rows))
			has_hash = False
			has_hash_known = False
			_g3 = 0
			_g2 = len(rows)
			while (_g3 < _g2):
				i = _g3
				_g3 = (_g3 + 1)
				row = (rows[i] if i >= 0 and i < len(rows) else None)
				if (not has_hash_known):
					if (len(python_Boot.fields(row)) == len(columns)):
						has_hash = True
					has_hash_known = True
				if (not has_hash):
					lst = row
					_g5 = 0
					_g4 = len(columns)
					while (_g5 < _g4):
						j = _g5
						_g5 = (_g5 + 1)
						val = (lst[j] if j >= 0 and j < len(lst) else None)
						output.setCell(j,i,Coopy.cellFor(val))
				else:
					_g51 = 0
					_g41 = len(columns)
					while (_g51 < _g41):
						j1 = _g51
						_g51 = (_g51 + 1)
						val1 = Reflect.field(row,(columns[j1] if j1 >= 0 and j1 < len(columns) else None))
						output.setCell(j1,i,Coopy.cellFor(val1))
		if (output is not None):
			output.trimBlank()
		return output

	@staticmethod
	def main():
		return 0

	@staticmethod
	def show(t):
		w = t.get_width()
		h = t.get_height()
		txt = ""
		_g = 0
		while (_g < h):
			y = _g
			_g = (_g + 1)
			_g1 = 0
			while (_g1 < w):
				x = _g1
				_g1 = (_g1 + 1)
				txt = (("null" if txt is None else txt) + Std.string(t.getCell(x,y)))
				txt = (("null" if txt is None else txt) + " ")
			txt = (("null" if txt is None else txt) + "\n")
		print(str(txt))

	@staticmethod
	def jsonify(t):
		workbook = haxe_ds_StringMap()
		sheet = list()
		w = t.get_width()
		h = t.get_height()
		txt = ""
		_g = 0
		while (_g < h):
			y = _g
			_g = (_g + 1)
			row = list()
			_g1 = 0
			while (_g1 < w):
				x = _g1
				_g1 = (_g1 + 1)
				v = t.getCell(x,y)
				row.append(v)
			sheet.append(row)
		workbook.h["sheet"] = sheet
		return workbook

Coopy._hx_class = Coopy


class CrossMatch:
	_hx_class_name = "CrossMatch"
	_hx_fields = ["spot_a", "spot_b", "item_a", "item_b"]

	def __init__(self):
		self.spot_a = None
		self.spot_b = None
		self.item_a = None
		self.item_b = None

CrossMatch._hx_class = CrossMatch


class Csv:
	_hx_class_name = "Csv"
	_hx_fields = ["cursor", "row_ended", "has_structure", "delim"]
	_hx_methods = ["renderTable", "renderCell", "parseTable", "makeTable", "parseCellPart", "parseCell"]

	def __init__(self,delim = ","):
		if (delim is None):
			delim = ","
		self.cursor = None
		self.row_ended = None
		self.has_structure = None
		self.delim = None
		self.cursor = 0
		self.row_ended = False
		if (delim is None):
			self.delim = ","
		else:
			self.delim = delim

	def renderTable(self,t):
		result = ""
		w = t.get_width()
		h = t.get_height()
		txt = ""
		v = t.getCellView()
		_g = 0
		while (_g < h):
			y = _g
			_g = (_g + 1)
			_g1 = 0
			while (_g1 < w):
				x = _g1
				_g1 = (_g1 + 1)
				if (x > 0):
					txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.delim))
				txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.renderCell(v,t.getCell(x,y))))
			txt = (("null" if txt is None else txt) + "\r\n")
		return txt

	def renderCell(self,v,d):
		if (d is None):
			return "NULL"
		_hx_str = v.toString(d)
		need_quote = False
		_g1 = 0
		_g = len(_hx_str)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			ch = None
			if ((i < 0) or ((i >= len(_hx_str)))):
				ch = ""
			else:
				ch = _hx_str[i]
			if (((((((ch == "\"") or ((ch == "'"))) or ((ch == self.delim))) or ((ch == "\r"))) or ((ch == "\n"))) or ((ch == "\t"))) or ((ch == " "))):
				need_quote = True
				break
		result = ""
		if need_quote:
			result = (("null" if result is None else result) + "\"")
		line_buf = ""
		_g11 = 0
		_g2 = len(_hx_str)
		while (_g11 < _g2):
			i1 = _g11
			_g11 = (_g11 + 1)
			ch1 = None
			if ((i1 < 0) or ((i1 >= len(_hx_str)))):
				ch1 = ""
			else:
				ch1 = _hx_str[i1]
			if (ch1 == "\""):
				result = (("null" if result is None else result) + "\"")
			if ((ch1 != "\r") and ((ch1 != "\n"))):
				if (len(line_buf) > 0):
					result = (("null" if result is None else result) + ("null" if line_buf is None else line_buf))
					line_buf = ""
				result = (("null" if result is None else result) + ("null" if ch1 is None else ch1))
			else:
				line_buf = (("null" if line_buf is None else line_buf) + ("null" if ch1 is None else ch1))
		if need_quote:
			result = (("null" if result is None else result) + "\"")
		return result

	def parseTable(self,txt,tab):
		if (not tab.isResizable()):
			return False
		self.cursor = 0
		self.row_ended = False
		self.has_structure = True
		tab.resize(0,0)
		w = 0
		h = 0
		at = 0
		yat = 0
		while (self.cursor < len(txt)):
			cell = self.parseCellPart(txt)
			if (yat >= h):
				h = (yat + 1)
				tab.resize(w,h)
			if (at >= w):
				w = (at + 1)
				tab.resize(w,h)
			tab.setCell(at,(h - 1),cell)
			at = (at + 1)
			if self.row_ended:
				at = 0
				yat = (yat + 1)
			_hx_local_2 = self
			_hx_local_3 = _hx_local_2.cursor
			_hx_local_2.cursor = (_hx_local_3 + 1)
			_hx_local_3
		return True

	def makeTable(self,txt):
		tab = SimpleTable(0, 0)
		self.parseTable(txt,tab)
		return tab

	def parseCellPart(self,txt):
		if (txt is None):
			return None
		self.row_ended = False
		first_non_underscore = len(txt)
		last_processed = 0
		quoting = False
		quote = 0
		result = ""
		start = self.cursor
		_g1 = self.cursor
		_g = len(txt)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			ch = HxString.charCodeAt(txt,i)
			last_processed = i
			if ((ch != 95) and ((i < first_non_underscore))):
				first_non_underscore = i
			if self.has_structure:
				if (not quoting):
					if (ch == HxString.charCodeAt(self.delim,0)):
						break
					if ((ch == 13) or ((ch == 10))):
						ch2 = HxString.charCodeAt(txt,(i + 1))
						if (ch2 is not None):
							if (ch2 != ch):
								if ((ch2 == 13) or ((ch2 == 10))):
									last_processed = (last_processed + 1)
						self.row_ended = True
						break
					if ((ch == 34) or ((ch == 39))):
						if (i == self.cursor):
							quoting = True
							quote = ch
							if (i != start):
								result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
							continue
						elif (ch == quote):
							quoting = True
					result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
					continue
				if (ch == quote):
					quoting = False
					continue
			result = (("null" if result is None else result) + HxOverrides.stringOrNull("".join(map(chr,[ch]))))
		self.cursor = last_processed
		if (quote == 0):
			if (result == "NULL"):
				return None
			if (first_non_underscore > start):
				_hx_del = (first_non_underscore - start)
				if (HxString.substr(result,_hx_del,None) == "NULL"):
					return HxString.substr(result,1,None)
		return result

	def parseCell(self,txt):
		self.cursor = 0
		self.row_ended = False
		self.has_structure = False
		return self.parseCellPart(txt)

Csv._hx_class = Csv


class Date:
	_hx_class_name = "Date"
	_hx_fields = ["date"]
	_hx_methods = ["toString"]

	def toString(self):
		m = ((self.date.month - 1) + 1)
		d = self.date.day
		h = self.date.hour
		mi = self.date.minute
		s = self.date.second
		return ((((((((((Std.string(self.date.year) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(m)) if ((m < 10)) else ("" + Std.string(m)))))) + "-") + HxOverrides.stringOrNull(((("0" + Std.string(d)) if ((d < 10)) else ("" + Std.string(d)))))) + " ") + HxOverrides.stringOrNull(((("0" + Std.string(h)) if ((h < 10)) else ("" + Std.string(h)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(mi)) if ((mi < 10)) else ("" + Std.string(mi)))))) + ":") + HxOverrides.stringOrNull(((("0" + Std.string(s)) if ((s < 10)) else ("" + Std.string(s))))))

Date._hx_class = Date


class DiffRender:
	_hx_class_name = "DiffRender"
	_hx_fields = ["text_to_insert", "td_open", "td_close", "open", "pretty_arrows", "section"]
	_hx_methods = ["usePrettyArrows", "insert", "beginTable", "setSection", "beginRow", "insertCell", "endRow", "endTable", "html", "toString", "render", "sampleCss", "completeHtml"]
	_hx_statics = ["examineCell", "markSpaces", "renderCell"]

	def __init__(self):
		self.text_to_insert = None
		self.td_open = None
		self.td_close = None
		self.open = None
		self.pretty_arrows = None
		self.section = None
		self.text_to_insert = list()
		self.open = False
		self.pretty_arrows = True

	def usePrettyArrows(self,flag):
		self.pretty_arrows = flag

	def insert(self,str):
		_this = self.text_to_insert
		_this.append(str)

	def beginTable(self):
		self.insert("<table>\n")
		self.section = None

	def setSection(self,str):
		if (str == self.section):
			return
		if (self.section is not None):
			self.insert("</t")
			self.insert(self.section)
			self.insert(">\n")
		self.section = str
		if (self.section is not None):
			self.insert("<t")
			self.insert(self.section)
			self.insert(">\n")

	def beginRow(self,mode):
		self.td_open = "<td"
		self.td_close = "</td>"
		row_class = ""
		if (mode == "header"):
			self.td_open = "<th"
			self.td_close = "</th>"
		row_class = mode
		tr = "<tr>"
		if (row_class != ""):
			tr = (("<tr class=\"" + ("null" if row_class is None else row_class)) + "\">")
		self.insert(tr)

	def insertCell(self,txt,mode):
		cell_decorate = ""
		if (mode != ""):
			cell_decorate = ((" class=\"" + ("null" if mode is None else mode)) + "\"")
		self.insert(((HxOverrides.stringOrNull(self.td_open) + ("null" if cell_decorate is None else cell_decorate)) + ">"))
		self.insert(txt)
		self.insert(self.td_close)

	def endRow(self):
		self.insert("</tr>\n")

	def endTable(self):
		self.setSection(None)
		self.insert("</table>\n")

	def html(self):
		return "".join([python_Boot.toString1(x1,'') for x1 in self.text_to_insert])

	def toString(self):
		return self.html()

	def render(self,tab):
		if ((tab.get_width() == 0) or ((tab.get_height() == 0))):
			return self
		render = self
		render.beginTable()
		change_row = -1
		cell = CellInfo()
		view = tab.getCellView()
		corner = view.toString(tab.getCell(0,0))
		off = None
		if (corner == "@:@"):
			off = 1
		else:
			off = 0
		if (off > 0):
			if ((tab.get_width() <= 1) or ((tab.get_height() <= 1))):
				return self
		_g1 = 0
		_g = tab.get_height()
		while (_g1 < _g):
			row = _g1
			_g1 = (_g1 + 1)
			open = False
			txt = view.toString(tab.getCell(off,row))
			if (txt is None):
				txt = ""
			DiffRender.examineCell(off,row,view,txt,"",txt,corner,cell,off)
			row_mode = cell.category
			if (row_mode == "spec"):
				change_row = row
			if (((row_mode == "header") or ((row_mode == "spec"))) or ((row_mode == "index"))):
				self.setSection("head")
			else:
				self.setSection("body")
			render.beginRow(row_mode)
			_g3 = 0
			_g2 = tab.get_width()
			while (_g3 < _g2):
				c = _g3
				_g3 = (_g3 + 1)
				DiffRender.examineCell(c,row,view,tab.getCell(c,row),(view.toString(tab.getCell(c,change_row)) if ((change_row >= 0)) else ""),txt,corner,cell,off)
				render.insertCell((cell.pretty_value if (self.pretty_arrows) else cell.value),cell.category_given_tr)
			render.endRow()
		render.endTable()
		return self

	def sampleCss(self):
		return ".highlighter .add { \n  background-color: #7fff7f;\n}\n\n.highlighter .remove { \n  background-color: #ff7f7f;\n}\n\n.highlighter td.modify { \n  background-color: #7f7fff;\n}\n\n.highlighter td.conflict { \n  background-color: #f00;\n}\n\n.highlighter .spec { \n  background-color: #aaa;\n}\n\n.highlighter .move { \n  background-color: #ffa;\n}\n\n.highlighter .null { \n  color: #888;\n}\n\n.highlighter table { \n  border-collapse:collapse;\n}\n\n.highlighter td, .highlighter th {\n  border: 1px solid #2D4068;\n  padding: 3px 7px 2px;\n}\n\n.highlighter th, .highlighter .header { \n  background-color: #aaf;\n  font-weight: bold;\n  padding-bottom: 4px;\n  padding-top: 5px;\n  text-align:left;\n}\n\n.highlighter tr.header th {\n  border-bottom: 2px solid black;\n}\n\n.highlighter tr.index td, .highlighter .index, .highlighter tr.header th.index {\n  background-color: white;\n  border: none;\n}\n\n.highlighter .gap {\n  color: #888;\n}\n\n.highlighter td {\n  empty-cells: show;\n}\n"

	def completeHtml(self):
		self.text_to_insert.insert(0, "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<style TYPE='text/css'>\n")
		x = self.sampleCss()
		self.text_to_insert.insert(1, x)
		self.text_to_insert.insert(2, "</style>\n</head>\n<body>\n<div class='highlighter'>\n")
		_this = self.text_to_insert
		_this.append("</div>\n</body>\n</html>\n")

	@staticmethod
	def examineCell(x,y,view,raw,vcol,vrow,vcorner,cell,offset = 0):
		if (offset is None):
			offset = 0
		nested = view.isHash(raw)
		value = None
		if (not nested):
			value = view.toString(raw)
		cell.category = ""
		cell.category_given_tr = ""
		cell.separator = ""
		cell.pretty_separator = ""
		cell.conflicted = False
		cell.updated = False
		def _hx_local_1():
			def _hx_local_0():
				cell.rvalue = None
				return cell.rvalue
			cell.lvalue = _hx_local_0()
			return cell.lvalue
		cell.pvalue = _hx_local_1()
		cell.value = value
		if (cell.value is None):
			cell.value = ""
		cell.pretty_value = cell.value
		if (vrow is None):
			vrow = ""
		if (vcol is None):
			vcol = ""
		removed_column = False
		if (vrow == ":"):
			cell.category = "move"
		if (((vrow == "") and ((offset == 1))) and ((y == 0))):
			cell.category = "index"
		if (vcol.find("+++") >= 0):
			def _hx_local_2():
				cell.category = "add"
				return cell.category
			cell.category_given_tr = _hx_local_2()
		elif (vcol.find("---") >= 0):
			def _hx_local_3():
				cell.category = "remove"
				return cell.category
			cell.category_given_tr = _hx_local_3()
			removed_column = True
		if (vrow == "!"):
			cell.category = "spec"
		elif (vrow == "@@"):
			cell.category = "header"
		elif (vrow == "..."):
			cell.category = "gap"
		elif (vrow == "+++"):
			if (not removed_column):
				cell.category = "add"
		elif (vrow == "---"):
			cell.category = "remove"
		elif (vrow.find("->") >= 0):
			if (not removed_column):
				tokens = vrow.split("!")
				full = vrow
				part = (tokens[1] if 1 < len(tokens) else None)
				if (part is None):
					part = full
				def _hx_local_4():
					_this = cell.value
					return _this.find(part)
				if (nested or ((_hx_local_4() >= 0))):
					cat = "modify"
					div = part
					if (part != full):
						if nested:
							cell.conflicted = view.hashExists(raw,"theirs")
						else:
							def _hx_local_5():
								_this1 = cell.value
								return _this1.find(full)
							cell.conflicted = (_hx_local_5() >= 0)
						if cell.conflicted:
							div = full
							cat = "conflict"
					cell.updated = True
					cell.separator = div
					cell.pretty_separator = div
					if nested:
						if cell.conflicted:
							tokens = [view.hashGet(raw,"before"), view.hashGet(raw,"ours"), view.hashGet(raw,"theirs")]
						else:
							tokens = [view.hashGet(raw,"before"), view.hashGet(raw,"after")]
					elif (cell.pretty_value == div):
						tokens = ["", ""]
					else:
						_this2 = cell.pretty_value
						if (div == ""):
							tokens = list(_this2)
						else:
							tokens = _this2.split(div)
					pretty_tokens = tokens
					if (len(tokens) >= 2):
						python_internal_ArrayImpl._set(pretty_tokens, 0, DiffRender.markSpaces((tokens[0] if 0 < len(tokens) else None),(tokens[1] if 1 < len(tokens) else None)))
						python_internal_ArrayImpl._set(pretty_tokens, 1, DiffRender.markSpaces((tokens[1] if 1 < len(tokens) else None),(tokens[0] if 0 < len(tokens) else None)))
					if (len(tokens) >= 3):
						ref = (pretty_tokens[0] if 0 < len(pretty_tokens) else None)
						python_internal_ArrayImpl._set(pretty_tokens, 0, DiffRender.markSpaces(ref,(tokens[2] if 2 < len(tokens) else None)))
						python_internal_ArrayImpl._set(pretty_tokens, 2, DiffRender.markSpaces((tokens[2] if 2 < len(tokens) else None),ref))
					cell.pretty_separator = "".join(map(chr,[8594]))
					cell.pretty_value = cell.pretty_separator.join([python_Boot.toString1(x1,'') for x1 in pretty_tokens])
					def _hx_local_6():
						cell.category = cat
						return cell.category
					cell.category_given_tr = _hx_local_6()
					offset1 = None
					if cell.conflicted:
						offset1 = 1
					else:
						offset1 = 0
					cell.lvalue = (tokens[offset1] if offset1 >= 0 and offset1 < len(tokens) else None)
					cell.rvalue = python_internal_ArrayImpl._get(tokens, (offset1 + 1))
					if cell.conflicted:
						cell.pvalue = (tokens[0] if 0 < len(tokens) else None)
		if ((x == 0) and ((offset > 0))):
			def _hx_local_7():
				cell.category = "index"
				return cell.category
			cell.category_given_tr = _hx_local_7()

	@staticmethod
	def markSpaces(sl,sr):
		if (sl == sr):
			return sl
		if ((sl is None) or ((sr is None))):
			return sl
		slc = StringTools.replace(sl," ","")
		src = StringTools.replace(sr," ","")
		if (slc != src):
			return sl
		slo = str("")
		il = 0
		ir = 0
		while (il < len(sl)):
			cl = None
			if ((il < 0) or ((il >= len(sl)))):
				cl = ""
			else:
				cl = sl[il]
			cr = ""
			if (ir < len(sr)):
				if ((ir < 0) or ((ir >= len(sr)))):
					cr = ""
				else:
					cr = sr[ir]
			if (cl == cr):
				slo = (("null" if slo is None else slo) + ("null" if cl is None else cl))
				il = (il + 1)
				ir = (ir + 1)
			elif (cr == " "):
				ir = (ir + 1)
			else:
				slo = (("null" if slo is None else slo) + HxOverrides.stringOrNull("".join(map(chr,[9251]))))
				il = (il + 1)
		return slo

	@staticmethod
	def renderCell(tab,view,x,y):
		cell = CellInfo()
		corner = view.toString(tab.getCell(0,0))
		off = None
		if (corner == "@:@"):
			off = 1
		else:
			off = 0
		DiffRender.examineCell(x,y,view,tab.getCell(x,y),view.toString(tab.getCell(x,off)),view.toString(tab.getCell(off,y)),corner,cell,off)
		return cell

DiffRender._hx_class = DiffRender


class EnumValue:
	_hx_class_name = "EnumValue"
EnumValue._hx_class = EnumValue


class FlatCellBuilder:
	_hx_class_name = "FlatCellBuilder"
	_hx_fields = ["view", "separator", "conflict_separator"]
	_hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "links"]
	_hx_statics = ["quoteForDiff"]
	_hx_interfaces = [CellBuilder]

	def __init__(self):
		self.view = None
		self.separator = None
		self.conflict_separator = None

	def needSeparator(self):
		return True

	def setSeparator(self,separator):
		self.separator = separator

	def setConflictSeparator(self,separator):
		self.conflict_separator = separator

	def setView(self,view):
		self.view = view

	def update(self,local,remote):
		return self.view.toDatum(((HxOverrides.stringOrNull(FlatCellBuilder.quoteForDiff(self.view,local)) + HxOverrides.stringOrNull(self.separator)) + HxOverrides.stringOrNull(FlatCellBuilder.quoteForDiff(self.view,remote))))

	def conflict(self,parent,local,remote):
		return ((((HxOverrides.stringOrNull(self.view.toString(parent)) + HxOverrides.stringOrNull(self.conflict_separator)) + HxOverrides.stringOrNull(self.view.toString(local))) + HxOverrides.stringOrNull(self.conflict_separator)) + HxOverrides.stringOrNull(self.view.toString(remote)))

	def marker(self,label):
		return self.view.toDatum(label)

	def links(self,unit):
		return self.view.toDatum(unit.toString())

	@staticmethod
	def quoteForDiff(v,d):
		nil = "NULL"
		if v.equals(d,None):
			return nil
		_hx_str = v.toString(d)
		score = 0
		_g1 = 0
		_g = len(_hx_str)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if (HxString.charCodeAt(_hx_str,score) != 95):
				break
			score = (score + 1)
		if (HxString.substr(_hx_str,score,None) == nil):
			_hx_str = ("_" + ("null" if _hx_str is None else _hx_str))
		return _hx_str

FlatCellBuilder._hx_class = FlatCellBuilder


class Row:
	_hx_class_name = "Row"
	_hx_methods = ["getRowString", "isPreamble"]
Row._hx_class = Row


class HighlightPatch:
	_hx_class_name = "HighlightPatch"
	_hx_fields = ["source", "patch", "view", "sourceView", "csv", "header", "headerPre", "headerPost", "headerRename", "headerMove", "modifier", "currentRow", "payloadCol", "payloadTop", "mods", "cmods", "rowInfo", "cellInfo", "rcOffset", "indexes", "sourceInPatchCol", "patchInSourceCol", "patchInSourceRow", "lastSourceRow", "actions", "rowPermutation", "rowPermutationRev", "colPermutation", "colPermutationRev", "haveDroppedColumns", "headerRow"]
	_hx_methods = ["reset", "apply", "needSourceColumns", "needSourceIndex", "applyRow", "getDatum", "getString", "applyMeta", "applyHeader", "lookUp", "applyAction", "checkAct", "getPreString", "getRowString", "isPreamble", "sortMods", "processMods", "computeOrdering", "permuteRows", "finishRows", "permuteColumns", "finishColumns"]
	_hx_interfaces = [Row]

	def __init__(self,source,patch):
		self.source = None
		self.patch = None
		self.view = None
		self.sourceView = None
		self.csv = None
		self.header = None
		self.headerPre = None
		self.headerPost = None
		self.headerRename = None
		self.headerMove = None
		self.modifier = None
		self.currentRow = None
		self.payloadCol = None
		self.payloadTop = None
		self.mods = None
		self.cmods = None
		self.rowInfo = None
		self.cellInfo = None
		self.rcOffset = None
		self.indexes = None
		self.sourceInPatchCol = None
		self.patchInSourceCol = None
		self.patchInSourceRow = None
		self.lastSourceRow = None
		self.actions = None
		self.rowPermutation = None
		self.rowPermutationRev = None
		self.colPermutation = None
		self.colPermutationRev = None
		self.haveDroppedColumns = None
		self.headerRow = None
		self.source = source
		self.patch = patch
		self.view = patch.getCellView()
		self.sourceView = source.getCellView()

	def reset(self):
		self.header = haxe_ds_IntMap()
		self.headerPre = haxe_ds_StringMap()
		self.headerPost = haxe_ds_StringMap()
		self.headerRename = haxe_ds_StringMap()
		self.headerMove = None
		self.modifier = haxe_ds_IntMap()
		self.mods = list()
		self.cmods = list()
		self.csv = Csv()
		self.rcOffset = 0
		self.currentRow = -1
		self.rowInfo = CellInfo()
		self.cellInfo = CellInfo()
		def _hx_local_0():
			self.patchInSourceCol = None
			return self.patchInSourceCol
		self.sourceInPatchCol = _hx_local_0()
		self.patchInSourceRow = haxe_ds_IntMap()
		self.indexes = None
		self.lastSourceRow = -1
		self.actions = list()
		self.rowPermutation = None
		self.rowPermutationRev = None
		self.colPermutation = None
		self.colPermutationRev = None
		self.haveDroppedColumns = False
		self.headerRow = 0

	def apply(self):
		self.reset()
		if (self.patch.get_width() < 2):
			return True
		if (self.patch.get_height() < 1):
			return True
		self.payloadCol = (1 + self.rcOffset)
		self.payloadTop = self.patch.get_width()
		corner = self.patch.getCellView().toString(self.patch.getCell(0,0))
		if (corner == "@:@"):
			self.rcOffset = 1
		else:
			self.rcOffset = 0
		_g1 = 0
		_g = self.patch.get_height()
		while (_g1 < _g):
			r = _g1
			_g1 = (_g1 + 1)
			_hx_str = self.view.toString(self.patch.getCell(self.rcOffset,r))
			_this = self.actions
			_this.append((_hx_str if ((_hx_str is not None)) else ""))
		self.headerRow = self.rcOffset
		_g11 = 0
		_g2 = self.patch.get_height()
		while (_g11 < _g2):
			r1 = _g11
			_g11 = (_g11 + 1)
			self.applyRow(r1)
		self.finishRows()
		self.finishColumns()
		return True

	def needSourceColumns(self):
		if (self.sourceInPatchCol is not None):
			return
		self.sourceInPatchCol = haxe_ds_IntMap()
		self.patchInSourceCol = haxe_ds_IntMap()
		av = self.source.getCellView()
		_g1 = 0
		_g = self.source.get_width()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			name = av.toString(self.source.getCell(i,0))
			at = self.headerPre.h.get(name,None)
			if (at is None):
				continue
			self.sourceInPatchCol.set(i,at)
			self.patchInSourceCol.set(at,i)

	def needSourceIndex(self):
		if (self.indexes is not None):
			return
		state = TableComparisonState()
		state.a = self.source
		state.b = self.source
		comp = CompareTable(state)
		comp.storeIndexes()
		comp.run()
		comp.align()
		self.indexes = comp.getIndexes()
		self.needSourceColumns()

	def applyRow(self,r):
		self.currentRow = r
		code = (self.actions[r] if r >= 0 and r < len(self.actions) else None)
		if ((r == 0) and ((self.rcOffset > 0))):
			pass
		elif (code == "@@"):
			self.headerRow = r
			self.applyHeader()
			self.applyAction("@@")
		elif (code == "!"):
			self.headerRow = r
			self.applyMeta()
		elif (code == "+++"):
			self.applyAction(code)
		elif (code == "---"):
			self.applyAction(code)
		elif ((code == "+") or ((code == ":"))):
			self.applyAction(code)
		elif (code.find("->") >= 0):
			self.applyAction("->")
		else:
			self.lastSourceRow = -1

	def getDatum(self,c):
		return self.patch.getCell(c,self.currentRow)

	def getString(self,c):
		return self.view.toString(self.getDatum(c))

	def applyMeta(self):
		_g1 = self.payloadCol
		_g = self.payloadTop
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			name = self.getString(i)
			if (name == ""):
				continue
			self.modifier.set(i,name)

	def applyHeader(self):
		_g1 = self.payloadCol
		_g = self.payloadTop
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			name = self.getString(i)
			if (name == "..."):
				self.modifier.set(i,"...")
				self.haveDroppedColumns = True
				continue
			mod = self.modifier.h.get(i,None)
			move = False
			if (mod is not None):
				if (HxString.charCodeAt(mod,0) == 58):
					move = True
					mod = HxString.substr(mod,1,len(mod))
			self.header.set(i,name)
			if (mod is not None):
				if (HxString.charCodeAt(mod,0) == 40):
					prev_name = HxString.substr(mod,1,(len(mod) - 2))
					self.headerPre.h[prev_name] = i
					self.headerPost.h[name] = i
					self.headerRename.h[prev_name] = name
					continue
			if (mod != "+++"):
				self.headerPre.h[name] = i
			if (mod != "---"):
				self.headerPost.h[name] = i
			if move:
				if (self.headerMove is None):
					self.headerMove = haxe_ds_StringMap()
				self.headerMove.h[name] = 1
		if (self.source.get_height() == 0):
			self.applyAction("+++")

	def lookUp(self,_hx_del = 0):
		if (_hx_del is None):
			_hx_del = 0
		at = self.patchInSourceRow.h.get((self.currentRow + _hx_del),None)
		if (at is not None):
			return at
		result = -1
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.currentRow
		_hx_local_0.currentRow = (_hx_local_1 + _hx_del)
		_hx_local_0.currentRow
		if ((self.currentRow >= 0) and ((self.currentRow < self.patch.get_height()))):
			_g = 0
			_g1 = self.indexes
			while (_g < len(_g1)):
				idx = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				match = idx.queryByContent(self)
				if (match.spot_a != 1):
					continue
				result = python_internal_ArrayImpl._get(match.item_a.lst, 0)
				break
		self.patchInSourceRow.set(self.currentRow,result)
		result
		_hx_local_3 = self
		_hx_local_4 = _hx_local_3.currentRow
		_hx_local_3.currentRow = (_hx_local_4 - _hx_del)
		_hx_local_3.currentRow
		return result

	def applyAction(self,code):
		mod = HighlightPatchUnit()
		mod.code = code
		mod.add = (code == "+++")
		mod.rem = (code == "---")
		mod.update = (code == "->")
		self.needSourceIndex()
		if (self.lastSourceRow == -1):
			self.lastSourceRow = self.lookUp(-1)
		mod.sourcePrevRow = self.lastSourceRow
		nextAct = python_internal_ArrayImpl._get(self.actions, (self.currentRow + 1))
		if ((nextAct != "+++") and ((nextAct != "..."))):
			mod.sourceNextRow = self.lookUp(1)
		if mod.add:
			if (python_internal_ArrayImpl._get(self.actions, (self.currentRow - 1)) != "+++"):
				mod.sourcePrevRow = self.lookUp(-1)
			mod.sourceRow = mod.sourcePrevRow
			if (mod.sourceRow != -1):
				mod.sourceRowOffset = 1
		else:
			def _hx_local_0():
				self.lastSourceRow = self.lookUp()
				return self.lastSourceRow
			mod.sourceRow = _hx_local_0()
		if (python_internal_ArrayImpl._get(self.actions, (self.currentRow + 1)) == ""):
			self.lastSourceRow = mod.sourceNextRow
		mod.patchRow = self.currentRow
		if (code == "@@"):
			mod.sourceRow = 0
		_this = self.mods
		_this.append(mod)

	def checkAct(self):
		act = self.getString(self.rcOffset)
		if (self.rowInfo.value != act):
			DiffRender.examineCell(0,0,self.view,act,"",act,"",self.rowInfo)

	def getPreString(self,txt):
		self.checkAct()
		if (not self.rowInfo.updated):
			return txt
		DiffRender.examineCell(0,0,self.view,txt,"",self.rowInfo.value,"",self.cellInfo)
		if (not self.cellInfo.updated):
			return txt
		return self.cellInfo.lvalue

	def getRowString(self,c):
		at = self.sourceInPatchCol.h.get(c,None)
		if (at is None):
			return "NOT_FOUND"
		return self.getPreString(self.getString(at))

	def isPreamble(self):
		return (self.currentRow <= self.headerRow)

	def sortMods(self,a,b):
		if ((b.code == "@@") and ((a.code != "@@"))):
			return 1
		if ((a.code == "@@") and ((b.code != "@@"))):
			return -1
		if (((a.sourceRow == -1) and (not a.add)) and ((b.sourceRow != -1))):
			return 1
		if (((a.sourceRow != -1) and (not b.add)) and ((b.sourceRow == -1))):
			return -1
		if ((a.sourceRow + a.sourceRowOffset) > ((b.sourceRow + b.sourceRowOffset))):
			return 1
		if ((a.sourceRow + a.sourceRowOffset) < ((b.sourceRow + b.sourceRowOffset))):
			return -1
		if (a.patchRow > b.patchRow):
			return 1
		if (a.patchRow < b.patchRow):
			return -1
		return 0

	def processMods(self,rmods,fate,len):
		rmods.sort(key= python_lib_Functools.cmp_to_key(self.sortMods))
		offset = 0
		last = -1
		target = 0
		if (len(rmods) > 0):
			if ((rmods[0] if 0 < len(rmods) else None).sourcePrevRow == -1):
				last = 0
		_g = 0
		while (_g < len(rmods)):
			mod = (rmods[_g] if _g >= 0 and _g < len(rmods) else None)
			_g = (_g + 1)
			if (last != -1):
				_g2 = last
				_g1 = (mod.sourceRow + mod.sourceRowOffset)
				while (_g2 < _g1):
					i = _g2
					_g2 = (_g2 + 1)
					fate.append((i + offset))
					target = (target + 1)
					last = (last + 1)
			if mod.rem:
				fate.append(-1)
				offset = (offset - 1)
			elif mod.add:
				mod.destRow = target
				target = (target + 1)
				offset = (offset + 1)
			else:
				mod.destRow = target
			if (mod.sourceRow >= 0):
				last = (mod.sourceRow + mod.sourceRowOffset)
				if mod.rem:
					last = (last + 1)
			else:
				last = -1
		if (last != -1):
			_g3 = last
			while (_g3 < len):
				i1 = _g3
				_g3 = (_g3 + 1)
				fate.append((i1 + offset))
				target = (target + 1)
				last = (last + 1)
		return (len + offset)

	def computeOrdering(self,mods,permutation,permutationRev,dim):
		to_unit = haxe_ds_IntMap()
		from_unit = haxe_ds_IntMap()
		meta_from_unit = haxe_ds_IntMap()
		ct = 0
		_g = 0
		while (_g < len(mods)):
			mod = (mods[_g] if _g >= 0 and _g < len(mods) else None)
			_g = (_g + 1)
			if (mod.add or mod.rem):
				continue
			if (mod.sourceRow < 0):
				continue
			if (mod.sourcePrevRow >= 0):
				v = mod.sourceRow
				to_unit.set(mod.sourcePrevRow,v)
				v
				v1 = mod.sourcePrevRow
				from_unit.set(mod.sourceRow,v1)
				v1
				if ((mod.sourcePrevRow + 1) != mod.sourceRow):
					ct = (ct + 1)
			if (mod.sourceNextRow >= 0):
				v2 = mod.sourceNextRow
				to_unit.set(mod.sourceRow,v2)
				v2
				v3 = mod.sourceRow
				from_unit.set(mod.sourceNextRow,v3)
				v3
				if ((mod.sourceRow + 1) != mod.sourceNextRow):
					ct = (ct + 1)
		if (ct > 0):
			cursor = None
			logical = None
			starts = []
			_g1 = 0
			while (_g1 < dim):
				i = _g1
				_g1 = (_g1 + 1)
				u = from_unit.h.get(i,None)
				if (u is not None):
					meta_from_unit.set(u,i)
					i
				else:
					starts.append(i)
			used = haxe_ds_IntMap()
			_hx_len = 0
			_g2 = 0
			while (_g2 < dim):
				i1 = _g2
				_g2 = (_g2 + 1)
				if logical in meta_from_unit.h:
					cursor = meta_from_unit.h.get(logical,None)
				else:
					cursor = None
				if (cursor is None):
					v4 = None
					v4 = (None if ((len(starts) == 0)) else starts.pop(0))
					cursor = v4
					logical = v4
				if (cursor is None):
					cursor = 0
				while cursor in used.h:
					cursor = (((cursor + 1)) % dim)
				logical = cursor
				permutationRev.append(cursor)
				used.set(cursor,1)
				1
			_g11 = 0
			_g3 = len(permutationRev)
			while (_g11 < _g3):
				i2 = _g11
				_g11 = (_g11 + 1)
				python_internal_ArrayImpl._set(permutation, i2, -1)
			_g12 = 0
			_g4 = len(permutation)
			while (_g12 < _g4):
				i3 = _g12
				_g12 = (_g12 + 1)
				python_internal_ArrayImpl._set(permutation, (permutationRev[i3] if i3 >= 0 and i3 < len(permutationRev) else None), i3)

	def permuteRows(self):
		self.rowPermutation = list()
		self.rowPermutationRev = list()
		self.computeOrdering(self.mods,self.rowPermutation,self.rowPermutationRev,self.source.get_height())

	def finishRows(self):
		fate = list()
		self.permuteRows()
		if (len(self.rowPermutation) > 0):
			_g = 0
			_g1 = self.mods
			while (_g < len(_g1)):
				mod = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
				_g = (_g + 1)
				if (mod.sourceRow >= 0):
					mod.sourceRow = python_internal_ArrayImpl._get(self.rowPermutation, mod.sourceRow)
		if (len(self.rowPermutation) > 0):
			self.source.insertOrDeleteRows(self.rowPermutation,len(self.rowPermutation))
		_hx_len = self.processMods(self.mods,fate,self.source.get_height())
		self.source.insertOrDeleteRows(fate,_hx_len)
		_g2 = 0
		_g11 = self.mods
		while (_g2 < len(_g11)):
			mod1 = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
			_g2 = (_g2 + 1)
			if (not mod1.rem):
				if mod1.add:
					_hx_local_2 = self.headerPost.iterator()
					while _hx_local_2.hasNext():
						c = _hx_local_2.next()
						offset = self.patchInSourceCol.h.get(c,None)
						if ((offset is not None) and ((offset >= 0))):
							self.source.setCell(offset,mod1.destRow,self.patch.getCell(c,mod1.patchRow))
				elif mod1.update:
					self.currentRow = mod1.patchRow
					self.checkAct()
					if (not self.rowInfo.updated):
						continue
					_hx_local_3 = self.headerPre.iterator()
					while _hx_local_3.hasNext():
						c1 = _hx_local_3.next()
						txt = self.view.toString(self.patch.getCell(c1,mod1.patchRow))
						DiffRender.examineCell(0,0,self.view,txt,"",self.rowInfo.value,"",self.cellInfo)
						if (not self.cellInfo.updated):
							continue
						if self.cellInfo.conflicted:
							continue
						d = self.view.toDatum(self.csv.parseCell(self.cellInfo.rvalue))
						self.source.setCell(self.patchInSourceCol.h.get(c1,None),mod1.destRow,d)

	def permuteColumns(self):
		if (self.headerMove is None):
			return
		self.colPermutation = list()
		self.colPermutationRev = list()
		self.computeOrdering(self.cmods,self.colPermutation,self.colPermutationRev,self.source.get_width())
		if (len(self.colPermutation) == 0):
			return

	def finishColumns(self):
		self.needSourceColumns()
		_g1 = self.payloadCol
		_g = self.payloadTop
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			act = self.modifier.h.get(i,None)
			hdr = self.header.h.get(i,None)
			if (act is None):
				act = ""
			if (act == "---"):
				at = self.patchInSourceCol.h.get(i,None)
				mod = HighlightPatchUnit()
				mod.code = act
				mod.rem = True
				mod.sourceRow = at
				mod.patchRow = i
				_this = self.cmods
				_this.append(mod)
			elif (act == "+++"):
				mod1 = HighlightPatchUnit()
				mod1.code = act
				mod1.add = True
				prev = -1
				cont = False
				mod1.sourceRow = -1
				if (len(self.cmods) > 0):
					mod1.sourceRow = python_internal_ArrayImpl._get(self.cmods, (len(self.cmods) - 1)).sourceRow
				if (mod1.sourceRow != -1):
					mod1.sourceRowOffset = 1
				mod1.patchRow = i
				_this1 = self.cmods
				_this1.append(mod1)
			elif (act != "..."):
				mod2 = HighlightPatchUnit()
				mod2.code = act
				mod2.patchRow = i
				mod2.sourceRow = self.patchInSourceCol.h.get(i,None)
				_this2 = self.cmods
				_this2.append(mod2)
		at1 = -1
		rat = -1
		_g11 = 0
		_g2 = (len(self.cmods) - 1)
		while (_g11 < _g2):
			i1 = _g11
			_g11 = (_g11 + 1)
			icode = (self.cmods[i1] if i1 >= 0 and i1 < len(self.cmods) else None).code
			if ((icode != "+++") and ((icode != "---"))):
				at1 = (self.cmods[i1] if i1 >= 0 and i1 < len(self.cmods) else None).sourceRow
			python_internal_ArrayImpl._get(self.cmods, (i1 + 1)).sourcePrevRow = at1
			j = ((len(self.cmods) - 1) - i1)
			jcode = (self.cmods[j] if j >= 0 and j < len(self.cmods) else None).code
			if ((jcode != "+++") and ((jcode != "---"))):
				rat = (self.cmods[j] if j >= 0 and j < len(self.cmods) else None).sourceRow
			python_internal_ArrayImpl._get(self.cmods, (j - 1)).sourceNextRow = rat
		fate = list()
		self.permuteColumns()
		if (self.headerMove is not None):
			if (len(self.colPermutation) > 0):
				_g3 = 0
				_g12 = self.cmods
				while (_g3 < len(_g12)):
					mod3 = (_g12[_g3] if _g3 >= 0 and _g3 < len(_g12) else None)
					_g3 = (_g3 + 1)
					if (mod3.sourceRow >= 0):
						mod3.sourceRow = python_internal_ArrayImpl._get(self.colPermutation, mod3.sourceRow)
				self.source.insertOrDeleteColumns(self.colPermutation,len(self.colPermutation))
		_hx_len = self.processMods(self.cmods,fate,self.source.get_width())
		self.source.insertOrDeleteColumns(fate,_hx_len)
		_g4 = 0
		_g13 = self.cmods
		while (_g4 < len(_g13)):
			cmod = (_g13[_g4] if _g4 >= 0 and _g4 < len(_g13) else None)
			_g4 = (_g4 + 1)
			if (not cmod.rem):
				if cmod.add:
					_g21 = 0
					_g31 = self.mods
					while (_g21 < len(_g31)):
						mod4 = (_g31[_g21] if _g21 >= 0 and _g21 < len(_g31) else None)
						_g21 = (_g21 + 1)
						if ((mod4.patchRow != -1) and ((mod4.destRow != -1))):
							d = self.patch.getCell(cmod.patchRow,mod4.patchRow)
							self.source.setCell(cmod.destRow,mod4.destRow,d)
					hdr1 = self.header.h.get(cmod.patchRow,None)
					self.source.setCell(cmod.destRow,0,self.view.toDatum(hdr1))
		_g14 = 0
		_g5 = self.source.get_width()
		while (_g14 < _g5):
			i2 = _g14
			_g14 = (_g14 + 1)
			name = self.view.toString(self.source.getCell(i2,0))
			next_name = self.headerRename.h.get(name,None)
			if (next_name is None):
				continue
			self.source.setCell(i2,0,self.view.toDatum(next_name))

HighlightPatch._hx_class = HighlightPatch


class HighlightPatchUnit:
	_hx_class_name = "HighlightPatchUnit"
	_hx_fields = ["add", "rem", "update", "code", "sourceRow", "sourceRowOffset", "sourcePrevRow", "sourceNextRow", "destRow", "patchRow"]
	_hx_methods = ["toString"]

	def __init__(self):
		self.add = None
		self.rem = None
		self.update = None
		self.code = None
		self.sourceRow = None
		self.sourceRowOffset = None
		self.sourcePrevRow = None
		self.sourceNextRow = None
		self.destRow = None
		self.patchRow = None
		self.add = False
		self.rem = False
		self.update = False
		self.sourceRow = -1
		self.sourceRowOffset = 0
		self.sourcePrevRow = -1
		self.sourceNextRow = -1
		self.destRow = -1
		self.patchRow = -1
		self.code = ""

	def toString(self):
		return ((((((((((HxOverrides.stringOrNull(self.code) + " patchRow ") + Std.string(self.patchRow)) + " sourceRows ") + Std.string(self.sourcePrevRow)) + ",") + Std.string(self.sourceRow)) + ",") + Std.string(self.sourceNextRow)) + " destRow ") + Std.string(self.destRow))

HighlightPatchUnit._hx_class = HighlightPatchUnit


class Index:
	_hx_class_name = "Index"
	_hx_fields = ["items", "keys", "top_freq", "height", "cols", "v", "indexed_table", "hdr"]
	_hx_methods = ["addColumn", "indexTable", "toKey", "toKeyByContent", "getTable"]

	def __init__(self):
		self.items = None
		self.keys = None
		self.top_freq = None
		self.height = None
		self.cols = None
		self.v = None
		self.indexed_table = None
		self.hdr = None
		self.items = haxe_ds_StringMap()
		self.cols = list()
		self.keys = list()
		self.top_freq = 0
		self.height = 0
		self.hdr = 0

	def addColumn(self,i):
		_this = self.cols
		_this.append(i)

	def indexTable(self,t,hdr):
		self.indexed_table = t
		self.hdr = hdr
		if ((len(self.keys) != t.get_height()) and ((t.get_height() > 0))):
			python_internal_ArrayImpl._set(self.keys, (t.get_height() - 1), None)
		_g1 = 0
		_g = t.get_height()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			key = (self.keys[i] if i >= 0 and i < len(self.keys) else None)
			if (key is None):
				key = self.toKey(t,i)
				python_internal_ArrayImpl._set(self.keys, i, key)
			item = self.items.h.get(key,None)
			if (item is None):
				item = IndexItem()
				self.items.h[key] = item
			ct = None
			if (item.lst is None):
				item.lst = list()
			_this = item.lst
			_this.append(i)
			ct = len(item.lst)
			if (ct > self.top_freq):
				self.top_freq = ct
		self.height = t.get_height()

	def toKey(self,t,i):
		wide = None
		if (i < self.hdr):
			wide = "_"
		else:
			wide = ""
		if (self.v is None):
			self.v = t.getCellView()
		_g1 = 0
		_g = len(self.cols)
		while (_g1 < _g):
			k = _g1
			_g1 = (_g1 + 1)
			d = t.getCell((self.cols[k] if k >= 0 and k < len(self.cols) else None),i)
			txt = self.v.toString(d)
			if ((((txt is None) or ((txt == ""))) or ((txt == "null"))) or ((txt == "undefined"))):
				continue
			if (k > 0):
				wide = (("null" if wide is None else wide) + " // ")
			wide = (("null" if wide is None else wide) + ("null" if txt is None else txt))
		return wide

	def toKeyByContent(self,row):
		wide = None
		if row.isPreamble():
			wide = "_"
		else:
			wide = ""
		_g1 = 0
		_g = len(self.cols)
		while (_g1 < _g):
			k = _g1
			_g1 = (_g1 + 1)
			txt = row.getRowString((self.cols[k] if k >= 0 and k < len(self.cols) else None))
			if ((((txt is None) or ((txt == ""))) or ((txt == "null"))) or ((txt == "undefined"))):
				continue
			if (k > 0):
				wide = (("null" if wide is None else wide) + " // ")
			wide = (("null" if wide is None else wide) + ("null" if txt is None else txt))
		return wide

	def getTable(self):
		return self.indexed_table

Index._hx_class = Index


class IndexItem:
	_hx_class_name = "IndexItem"
	_hx_fields = ["lst"]
	_hx_methods = ["add", "length", "value"]

	def __init__(self):
		self.lst = None

	def add(self,i):
		if (self.lst is None):
			self.lst = list()
		_this = self.lst
		_this.append(i)
		return len(self.lst)

	def length(self):
		return len(self.lst)

	def value(self):
		return (self.lst[0] if 0 < len(self.lst) else None)

IndexItem._hx_class = IndexItem


class IndexPair:
	_hx_class_name = "IndexPair"
	_hx_fields = ["ia", "ib", "hdr", "quality"]
	_hx_methods = ["addColumns", "indexTables", "queryByKey", "queryByContent", "queryLocal", "localKey", "remoteKey", "getTopFreq", "getQuality"]

	def __init__(self):
		self.ia = None
		self.ib = None
		self.hdr = None
		self.quality = None
		self.ia = Index()
		self.ib = Index()
		self.quality = 0
		self.hdr = 0

	def addColumns(self,ca,cb):
		self.ia.addColumn(ca)
		self.ib.addColumn(cb)

	def indexTables(self,a,b,hdr):
		self.ia.indexTable(a,hdr)
		self.ib.indexTable(b,hdr)
		self.hdr = hdr
		good = 0
		_hx_local_1 = self.ia.items.keys()
		while _hx_local_1.hasNext():
			key = _hx_local_1.next()
			item_a = self.ia.items.h.get(key,None)
			spot_a = len(item_a.lst)
			item_b = self.ib.items.h.get(key,None)
			spot_b = 0
			if (item_b is not None):
				spot_b = len(item_b.lst)
			if ((spot_a == 1) and ((spot_b == 1))):
				good = (good + 1)
		def _hx_local_2():
			b1 = a.get_height()
			return (1.0 if (python_lib_Math.isnan(1.0)) else (b1 if (python_lib_Math.isnan(b1)) else max(1.0,b1)))
		self.quality = (good / _hx_local_2())

	def queryByKey(self,ka):
		result = CrossMatch()
		result.item_a = self.ia.items.h.get(ka,None)
		result.item_b = self.ib.items.h.get(ka,None)
		def _hx_local_0():
			result.spot_b = 0
			return result.spot_b
		result.spot_a = _hx_local_0()
		if (ka != ""):
			if (result.item_a is not None):
				result.spot_a = len(result.item_a.lst)
			if (result.item_b is not None):
				result.spot_b = len(result.item_b.lst)
		return result

	def queryByContent(self,row):
		result = CrossMatch()
		ka = self.ia.toKeyByContent(row)
		return self.queryByKey(ka)

	def queryLocal(self,row):
		ka = self.ia.toKey(self.ia.getTable(),row)
		return self.queryByKey(ka)

	def localKey(self,row):
		return self.ia.toKey(self.ia.getTable(),row)

	def remoteKey(self,row):
		return self.ib.toKey(self.ib.getTable(),row)

	def getTopFreq(self):
		if (self.ib.top_freq > self.ia.top_freq):
			return self.ib.top_freq
		return self.ia.top_freq

	def getQuality(self):
		return self.quality

IndexPair._hx_class = IndexPair


class Lambda:
	_hx_class_name = "Lambda"
	_hx_statics = ["array", "map", "has"]

	@staticmethod
	def array(it):
		a = list()
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			a.append(i)
		return a

	@staticmethod
	def map(it,f):
		l = List()
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			l.add(f(x))
		return l

	@staticmethod
	def has(it,elt):
		_hx_local_0 = HxOverrides.iterator(it)
		while _hx_local_0.hasNext():
			x = _hx_local_0.next()
			if (x == elt):
				return True
		return False
Lambda._hx_class = Lambda


class List:
	_hx_class_name = "List"
	_hx_fields = ["h", "q", "length"]
	_hx_methods = ["add", "iterator"]

	def __init__(self):
		self.h = None
		self.q = None
		self.length = None
		self.length = 0

	def add(self,item):
		x = [item]
		if (self.h is None):
			self.h = x
		else:
			python_internal_ArrayImpl._set(self.q, 1, x)
		self.q = x
		_hx_local_0 = self
		_hx_local_1 = _hx_local_0.length
		_hx_local_0.length = (_hx_local_1 + 1)
		_hx_local_1

	def iterator(self):
		return _List_ListIterator(self.h)

List._hx_class = List


class _List_ListIterator:
	_hx_class_name = "_List.ListIterator"
	_hx_fields = ["head", "val"]
	_hx_methods = ["hasNext", "next"]

	def __init__(self,head):
		self.head = None
		self.val = None
		self.head = head
		self.val = None

	def hasNext(self):
		return (self.head is not None)

	def next(self):
		self.val = (self.head[0] if 0 < len(self.head) else None)
		self.head = (self.head[1] if 1 < len(self.head) else None)
		return self.val

_List_ListIterator._hx_class = _List_ListIterator


class Merger:
	_hx_class_name = "Merger"
	_hx_fields = ["parent", "local", "remote", "flags", "order", "units", "column_order", "column_units", "row_mix_local", "row_mix_remote", "column_mix_local", "column_mix_remote", "conflicts"]
	_hx_methods = ["shuffleDimension", "shuffleColumns", "shuffleRows", "apply"]
	_hx_statics = ["makeConflictedCell"]

	def __init__(self,parent,local,remote,flags):
		self.parent = None
		self.local = None
		self.remote = None
		self.flags = None
		self.order = None
		self.units = None
		self.column_order = None
		self.column_units = None
		self.row_mix_local = None
		self.row_mix_remote = None
		self.column_mix_local = None
		self.column_mix_remote = None
		self.conflicts = None
		self.parent = parent
		self.local = local
		self.remote = remote
		self.flags = flags

	def shuffleDimension(self,dim_units,len,fate,cl,cr):
		at = 0
		_g = 0
		while (_g < len(dim_units)):
			cunit = (dim_units[_g] if _g >= 0 and _g < len(dim_units) else None)
			_g = (_g + 1)
			if (cunit.p < 0):
				if (cunit.l < 0):
					if (cunit.r >= 0):
						cr.set(cunit.r,at)
						at
						at = (at + 1)
				else:
					cl.set(cunit.l,at)
					at
					at = (at + 1)
			elif (cunit.l >= 0):
				if (cunit.r < 0):
					pass
				else:
					cl.set(cunit.l,at)
					at
					at = (at + 1)
		_g1 = 0
		while (_g1 < len):
			x = _g1
			_g1 = (_g1 + 1)
			idx = cl.h.get(x,None)
			if (idx is None):
				fate.append(-1)
			else:
				fate.append(idx)
		return at

	def shuffleColumns(self):
		self.column_mix_local = haxe_ds_IntMap()
		self.column_mix_remote = haxe_ds_IntMap()
		fate = list()
		wfate = self.shuffleDimension(self.column_units,self.local.get_width(),fate,self.column_mix_local,self.column_mix_remote)
		self.local.insertOrDeleteColumns(fate,wfate)

	def shuffleRows(self):
		self.row_mix_local = haxe_ds_IntMap()
		self.row_mix_remote = haxe_ds_IntMap()
		fate = list()
		hfate = self.shuffleDimension(self.units,self.local.get_height(),fate,self.row_mix_local,self.row_mix_remote)
		self.local.insertOrDeleteRows(fate,hfate)

	def apply(self):
		self.conflicts = 0
		ct = Coopy.compareTables3(self.parent,self.local,self.remote)
		align = ct.align()
		self.order = align.toOrder()
		self.units = self.order.getList()
		self.column_order = align.meta.toOrder()
		self.column_units = self.column_order.getList()
		allow_insert = self.flags.allowInsert()
		allow_delete = self.flags.allowDelete()
		allow_update = self.flags.allowUpdate()
		view = self.parent.getCellView()
		_g = 0
		_g1 = self.units
		while (_g < len(_g1)):
			row = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if (((row.l >= 0) and ((row.r >= 0))) and ((row.p >= 0))):
				_g2 = 0
				_g3 = self.column_units
				while (_g2 < len(_g3)):
					col = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
					_g2 = (_g2 + 1)
					if (((col.l >= 0) and ((col.r >= 0))) and ((col.p >= 0))):
						pcell = self.parent.getCell(col.p,row.p)
						rcell = self.remote.getCell(col.r,row.r)
						if (not view.equals(pcell,rcell)):
							lcell = self.local.getCell(col.l,row.l)
							if view.equals(pcell,lcell):
								self.local.setCell(col.l,row.l,rcell)
							else:
								self.local.setCell(col.l,row.l,Merger.makeConflictedCell(view,pcell,lcell,rcell))
								_hx_local_2 = self
								_hx_local_3 = _hx_local_2.conflicts
								_hx_local_2.conflicts = (_hx_local_3 + 1)
								_hx_local_3
		self.shuffleColumns()
		self.shuffleRows()
		_hx_local_5 = self.column_mix_remote.keys()
		while _hx_local_5.hasNext():
			x = _hx_local_5.next()
			x2 = self.column_mix_remote.h.get(x,None)
			_g4 = 0
			_g11 = self.units
			while (_g4 < len(_g11)):
				unit = (_g11[_g4] if _g4 >= 0 and _g4 < len(_g11) else None)
				_g4 = (_g4 + 1)
				if ((unit.l >= 0) and ((unit.r >= 0))):
					self.local.setCell(x2,self.row_mix_local.h.get(unit.l,None),self.remote.getCell(x,unit.r))
				elif ((unit.p < 0) and ((unit.r >= 0))):
					self.local.setCell(x2,self.row_mix_remote.h.get(unit.r,None),self.remote.getCell(x,unit.r))
		_hx_local_7 = self.row_mix_remote.keys()
		while _hx_local_7.hasNext():
			y = _hx_local_7.next()
			y2 = self.row_mix_remote.h.get(y,None)
			_g5 = 0
			_g12 = self.column_units
			while (_g5 < len(_g12)):
				unit1 = (_g12[_g5] if _g5 >= 0 and _g5 < len(_g12) else None)
				_g5 = (_g5 + 1)
				if ((unit1.l >= 0) and ((unit1.r >= 0))):
					self.local.setCell(self.column_mix_local.h.get(unit1.l,None),y2,self.remote.getCell(unit1.r,y))
		return self.conflicts

	@staticmethod
	def makeConflictedCell(view,pcell,lcell,rcell):
		return view.toDatum(((((("((( " + HxOverrides.stringOrNull(view.toString(pcell))) + " ))) ") + HxOverrides.stringOrNull(view.toString(lcell))) + " /// ") + HxOverrides.stringOrNull(view.toString(rcell))))

Merger._hx_class = Merger


class Mover:
	_hx_class_name = "Mover"
	_hx_statics = ["moveUnits", "move", "moveWithoutExtras"]

	@staticmethod
	def moveUnits(units):
		isrc = list()
		idest = list()
		_hx_len = len(units)
		ltop = -1
		rtop = -1
		in_src = haxe_ds_IntMap()
		in_dest = haxe_ds_IntMap()
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			unit = (units[i] if i >= 0 and i < len(units) else None)
			if ((unit.l >= 0) and ((unit.r >= 0))):
				if (ltop < unit.l):
					ltop = unit.l
				if (rtop < unit.r):
					rtop = unit.r
				in_src.set(unit.l,i)
				i
				in_dest.set(unit.r,i)
				i
		v = None
		_g1 = 0
		_g2 = (ltop + 1)
		while (_g1 < _g2):
			i1 = _g1
			_g1 = (_g1 + 1)
			v = in_src.h.get(i1,None)
			if (v is not None):
				isrc.append(v)
		_g11 = 0
		_g3 = (rtop + 1)
		while (_g11 < _g3):
			i2 = _g11
			_g11 = (_g11 + 1)
			v = in_dest.h.get(i2,None)
			if (v is not None):
				idest.append(v)
		return Mover.moveWithoutExtras(isrc,idest)

	@staticmethod
	def move(isrc,idest):
		_hx_len = len(isrc)
		len2 = len(idest)
		in_src = haxe_ds_IntMap()
		in_dest = haxe_ds_IntMap()
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			in_src.set((isrc[i] if i >= 0 and i < len(isrc) else None),i)
			i
		_g1 = 0
		while (_g1 < len2):
			i1 = _g1
			_g1 = (_g1 + 1)
			in_dest.set((idest[i1] if i1 >= 0 and i1 < len(idest) else None),i1)
			i1
		src = list()
		dest = list()
		v = None
		_g2 = 0
		while (_g2 < _hx_len):
			i2 = _g2
			_g2 = (_g2 + 1)
			v = (isrc[i2] if i2 >= 0 and i2 < len(isrc) else None)
			if v in in_dest.h:
				src.append(v)
		_g3 = 0
		while (_g3 < len2):
			i3 = _g3
			_g3 = (_g3 + 1)
			v = (idest[i3] if i3 >= 0 and i3 < len(idest) else None)
			if v in in_src.h:
				dest.append(v)
		return Mover.moveWithoutExtras(src,dest)

	@staticmethod
	def moveWithoutExtras(src,dest):
		if (len(src) != len(dest)):
			return None
		if (len(src) <= 1):
			return []
		_hx_len = len(src)
		in_src = haxe_ds_IntMap()
		blk_len = haxe_ds_IntMap()
		blk_src_loc = haxe_ds_IntMap()
		blk_dest_loc = haxe_ds_IntMap()
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			in_src.set((src[i] if i >= 0 and i < len(src) else None),i)
			i
		ct = 0
		in_cursor = -2
		out_cursor = 0
		next = None
		blk = -1
		v = None
		while (out_cursor < _hx_len):
			v = (dest[out_cursor] if out_cursor >= 0 and out_cursor < len(dest) else None)
			next = in_src.h.get(v,None)
			if (next != ((in_cursor + 1))):
				blk = v
				ct = 1
				blk_src_loc.set(blk,next)
				blk_dest_loc.set(blk,out_cursor)
			else:
				ct = (ct + 1)
			blk_len.set(blk,ct)
			in_cursor = next
			out_cursor = (out_cursor + 1)
		blks = list()
		_hx_local_2 = blk_len.keys()
		while _hx_local_2.hasNext():
			k = _hx_local_2.next()
			blks.append(k)
		def _hx_local_3(a,b):
			return (blk_len.h.get(b,None) - blk_len.h.get(a,None))
		blks.sort(key= python_lib_Functools.cmp_to_key(_hx_local_3))
		moved = list()
		while (len(blks) > 0):
			blk1 = None
			blk1 = (None if ((len(blks) == 0)) else blks.pop(0))
			blen = len(blks)
			ref_src_loc = blk_src_loc.h.get(blk1,None)
			ref_dest_loc = blk_dest_loc.h.get(blk1,None)
			i1 = (blen - 1)
			while (i1 >= 0):
				blki = (blks[i1] if i1 >= 0 and i1 < len(blks) else None)
				blki_src_loc = blk_src_loc.h.get(blki,None)
				to_left_src = (blki_src_loc < ref_src_loc)
				to_left_dest = (blk_dest_loc.h.get(blki,None) < ref_dest_loc)
				if (to_left_src != to_left_dest):
					ct1 = blk_len.h.get(blki,None)
					_g1 = 0
					while (_g1 < ct1):
						j = _g1
						_g1 = (_g1 + 1)
						moved.append((src[blki_src_loc] if blki_src_loc >= 0 and blki_src_loc < len(src) else None))
						blki_src_loc = (blki_src_loc + 1)
					pos = i1
					if (pos < 0):
						pos = (len(blks) + pos)
					if (pos < 0):
						pos = 0
					res = blks[pos:(pos + 1)]
					del blks[pos:(pos + 1)]
					res
				i1 = (i1 - 1)
		return moved
Mover._hx_class = Mover


class Ndjson:
	_hx_class_name = "Ndjson"
	_hx_fields = ["tab", "view", "columns", "header_row"]
	_hx_methods = ["renderRow", "render", "addRow", "addHeaderRow", "parse"]

	def __init__(self,tab):
		self.tab = None
		self.view = None
		self.columns = None
		self.header_row = None
		self.tab = tab
		self.view = tab.getCellView()
		self.header_row = 0

	def renderRow(self,r):
		row = haxe_ds_StringMap()
		_g1 = 0
		_g = self.tab.get_width()
		while (_g1 < _g):
			c = _g1
			_g1 = (_g1 + 1)
			key = self.view.toString(self.tab.getCell(c,self.header_row))
			if ((c == 0) and ((self.header_row == 1))):
				key = "@:@"
			value = self.tab.getCell(c,r)
			value1 = value
			row.h[key] = value1
		return haxe_format_JsonPrinter.print(row,None,None)

	def render(self):
		txt = ""
		offset = 0
		if (self.tab.get_height() == 0):
			return txt
		if (self.tab.get_width() == 0):
			return txt
		if (self.tab.getCell(0,0) == "@:@"):
			offset = 1
		self.header_row = offset
		_g1 = (self.header_row + 1)
		_g = self.tab.get_height()
		while (_g1 < _g):
			r = _g1
			_g1 = (_g1 + 1)
			txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.renderRow(r)))
			txt = (("null" if txt is None else txt) + "\n")
		return txt

	def addRow(self,r,txt):
		json = python_lib_Json.loads(txt,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
		if (self.columns is None):
			self.columns = haxe_ds_StringMap()
		w = self.tab.get_width()
		h = self.tab.get_height()
		resize = False
		_g = 0
		_g1 = python_Boot.fields(json)
		while (_g < len(_g1)):
			name = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if (not name in self.columns.h):
				self.columns.h[name] = w
				w = (w + 1)
				resize = True
		if (r >= h):
			h = (r + 1)
			resize = True
		if resize:
			self.tab.resize(w,h)
		_g2 = 0
		_g11 = python_Boot.fields(json)
		while (_g2 < len(_g11)):
			name1 = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
			_g2 = (_g2 + 1)
			v = Reflect.field(json,name1)
			c = self.columns.h.get(name1,None)
			self.tab.setCell(c,r,v)

	def addHeaderRow(self,r):
		names = self.columns.keys()
		_hx_local_0 = names
		while _hx_local_0.hasNext():
			n = _hx_local_0.next()
			self.tab.setCell(self.columns.h.get(n,None),r,self.view.toDatum(n))

	def parse(self,txt):
		self.columns = None
		rows = txt.split("\n")
		h = len(rows)
		if (h == 0):
			self.tab.clear()
			return
		if (python_internal_ArrayImpl._get(rows, (h - 1)) == ""):
			h = (h - 1)
		_g = 0
		while (_g < h):
			i = _g
			_g = (_g + 1)
			at = ((h - i) - 1)
			self.addRow((at + 1),(rows[at] if at >= 0 and at < len(rows) else None))
		self.addHeaderRow(0)

Ndjson._hx_class = Ndjson


class NestedCellBuilder:
	_hx_class_name = "NestedCellBuilder"
	_hx_fields = ["view"]
	_hx_methods = ["needSeparator", "setSeparator", "setConflictSeparator", "setView", "update", "conflict", "marker", "negToNull", "links"]
	_hx_interfaces = [CellBuilder]

	def __init__(self):
		self.view = None

	def needSeparator(self):
		return False

	def setSeparator(self,separator):
		pass

	def setConflictSeparator(self,separator):
		pass

	def setView(self,view):
		self.view = view

	def update(self,local,remote):
		h = self.view.makeHash()
		self.view.hashSet(h,"before",local)
		self.view.hashSet(h,"after",remote)
		return h

	def conflict(self,parent,local,remote):
		h = self.view.makeHash()
		self.view.hashSet(h,"before",parent)
		self.view.hashSet(h,"ours",local)
		self.view.hashSet(h,"theirs",remote)
		return h

	def marker(self,label):
		return self.view.toDatum(label)

	def negToNull(self,x):
		if (x < 0):
			return None
		return x

	def links(self,unit):
		h = self.view.makeHash()
		if (unit.p >= -1):
			self.view.hashSet(h,"before",self.negToNull(unit.p))
			self.view.hashSet(h,"ours",self.negToNull(unit.l))
			self.view.hashSet(h,"theirs",self.negToNull(unit.r))
			return h
		self.view.hashSet(h,"before",self.negToNull(unit.l))
		self.view.hashSet(h,"after",self.negToNull(unit.r))
		return h

NestedCellBuilder._hx_class = NestedCellBuilder


class Ordering:
	_hx_class_name = "Ordering"
	_hx_fields = ["order", "ignore_parent"]
	_hx_methods = ["add", "getList", "toString", "ignoreParent"]

	def __init__(self):
		self.order = None
		self.ignore_parent = None
		self.order = list()
		self.ignore_parent = False

	def add(self,l,r,p = -2):
		if (p is None):
			p = -2
		if self.ignore_parent:
			p = -2
		_this = self.order
		x = Unit(l, r, p)
		_this.append(x)

	def getList(self):
		return self.order

	def toString(self):
		txt = ""
		_g1 = 0
		_g = len(self.order)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if (i > 0):
				txt = (("null" if txt is None else txt) + ", ")
			txt = (("null" if txt is None else txt) + Std.string((self.order[i] if i >= 0 and i < len(self.order) else None)))
		return txt

	def ignoreParent(self):
		self.ignore_parent = True

Ordering._hx_class = Ordering


class Reflect:
	_hx_class_name = "Reflect"
	_hx_statics = ["field", "isFunction"]

	@staticmethod
	def field(o,field):
		return python_Boot.field(o,field)

	@staticmethod
	def isFunction(f):
		return ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)) or hasattr(f,"func_code"))
Reflect._hx_class = Reflect


class Table:
	_hx_class_name = "Table"
	_hx_methods = ["getCell", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone"]
Table._hx_class = Table


class SimpleTable:
	_hx_class_name = "SimpleTable"
	_hx_fields = ["data", "w", "h"]
	_hx_methods = ["getTable", "get_width", "get_height", "getCell", "setCell", "toString", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "getData", "clone"]
	_hx_statics = ["tableToString", "tableIsSimilar"]
	_hx_interfaces = [Table]

	def __init__(self,w,h):
		self.data = None
		self.w = None
		self.h = None
		self.data = haxe_ds_IntMap()
		self.w = w
		self.h = h

	def getTable(self):
		return self

	def get_width(self):
		return self.w

	def get_height(self):
		return self.h

	def getCell(self,x,y):
		return self.data.h.get((x + ((y * self.w))),None)

	def setCell(self,x,y,c):
		value = c
		self.data.set((x + ((y * self.w))),value)

	def toString(self):
		return SimpleTable.tableToString(self)

	def getCellView(self):
		return SimpleView()

	def isResizable(self):
		return True

	def resize(self,w,h):
		self.w = w
		self.h = h
		return True

	def clear(self):
		self.data = haxe_ds_IntMap()

	def insertOrDeleteRows(self,fate,hfate):
		data2 = haxe_ds_IntMap()
		_g1 = 0
		_g = len(fate)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			j = (fate[i] if i >= 0 and i < len(fate) else None)
			if (j != -1):
				_g3 = 0
				_g2 = self.w
				while (_g3 < _g2):
					c = _g3
					_g3 = (_g3 + 1)
					idx = ((i * self.w) + c)
					if idx in self.data.h:
						value = self.data.h.get(idx,None)
						data2.set(((j * self.w) + c),value)
		self.h = hfate
		self.data = data2
		return True

	def insertOrDeleteColumns(self,fate,wfate):
		data2 = haxe_ds_IntMap()
		_g1 = 0
		_g = len(fate)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			j = (fate[i] if i >= 0 and i < len(fate) else None)
			if (j != -1):
				_g3 = 0
				_g2 = self.h
				while (_g3 < _g2):
					r = _g3
					_g3 = (_g3 + 1)
					idx = ((r * self.w) + i)
					if idx in self.data.h:
						value = self.data.h.get(idx,None)
						data2.set(((r * wfate) + j),value)
		self.w = wfate
		self.data = data2
		return True

	def trimBlank(self):
		if (self.h == 0):
			return True
		h_test = self.h
		if (h_test >= 3):
			h_test = 3
		view = self.getCellView()
		space = view.toDatum("")
		more = True
		while more:
			_g1 = 0
			_g = self.get_width()
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				c = self.getCell(i,(self.h - 1))
				if (not ((view.equals(c,space) or ((c is None))))):
					more = False
					break
			if more:
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.h
				_hx_local_0.h = (_hx_local_1 - 1)
				_hx_local_1
		more = True
		nw = self.w
		while more:
			if (self.w == 0):
				break
			_g2 = 0
			while (_g2 < h_test):
				i1 = _g2
				_g2 = (_g2 + 1)
				c1 = self.getCell((nw - 1),i1)
				if (not ((view.equals(c1,space) or ((c1 is None))))):
					more = False
					break
			if more:
				nw = (nw - 1)
		if (nw == self.w):
			return True
		data2 = haxe_ds_IntMap()
		_g3 = 0
		while (_g3 < nw):
			i2 = _g3
			_g3 = (_g3 + 1)
			_g21 = 0
			_g11 = self.h
			while (_g21 < _g11):
				r = _g21
				_g21 = (_g21 + 1)
				idx = ((r * self.w) + i2)
				if idx in self.data.h:
					value = self.data.h.get(idx,None)
					data2.set(((r * nw) + i2),value)
		self.w = nw
		self.data = data2
		return True

	def getData(self):
		return None

	def clone(self):
		result = SimpleTable(self.get_width(), self.get_height())
		_g1 = 0
		_g = self.get_height()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_g3 = 0
			_g2 = self.get_width()
			while (_g3 < _g2):
				j = _g3
				_g3 = (_g3 + 1)
				result.setCell(j,i,self.getCell(j,i))
		return result

	@staticmethod
	def tableToString(tab):
		x = ""
		_g1 = 0
		_g = tab.get_height()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_g3 = 0
			_g2 = tab.get_width()
			while (_g3 < _g2):
				j = _g3
				_g3 = (_g3 + 1)
				if (j > 0):
					x = (("null" if x is None else x) + " ")
				x = (("null" if x is None else x) + Std.string(tab.getCell(j,i)))
			x = (("null" if x is None else x) + "\n")
		return x

	@staticmethod
	def tableIsSimilar(tab1,tab2):
		if (tab1.get_width() != tab2.get_width()):
			return False
		if (tab1.get_height() != tab2.get_height()):
			return False
		v = tab1.getCellView()
		_g1 = 0
		_g = tab1.get_height()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			_g3 = 0
			_g2 = tab1.get_width()
			while (_g3 < _g2):
				j = _g3
				_g3 = (_g3 + 1)
				if (not v.equals(tab1.getCell(j,i),tab2.getCell(j,i))):
					return False
		return True

SimpleTable._hx_class = SimpleTable


class View:
	_hx_class_name = "View"
	_hx_methods = ["toString", "equals", "toDatum", "makeHash", "hashSet", "isHash", "hashExists", "hashGet"]
View._hx_class = View


class SimpleView:
	_hx_class_name = "SimpleView"
	_hx_methods = ["toString", "equals", "toDatum", "makeHash", "hashSet", "hashExists", "hashGet", "isHash"]
	_hx_interfaces = [View]

	def __init__(self):
		pass

	def toString(self,d):
		if (d is None):
			return None
		return ("" + Std.string(d))

	def equals(self,d1,d2):
		if ((d1 is None) and ((d2 is None))):
			return True
		if ((d1 is None) and ((("" + Std.string(d2)) == ""))):
			return True
		if ((("" + Std.string(d1)) == "") and ((d2 is None))):
			return True
		return (("" + Std.string(d1)) == (("" + Std.string(d2))))

	def toDatum(self,x):
		return x

	def makeHash(self):
		return haxe_ds_StringMap()

	def hashSet(self,h,str,d):
		hh = h
		value = d
		value1 = value
		hh.h[str] = value1

	def hashExists(self,h,str):
		hh = h
		return str in hh.h

	def hashGet(self,h,str):
		hh = h
		return hh.h.get(str,None)

	def isHash(self,h):
		return Std._hx_is(h,haxe_ds_StringMap)

SimpleView._hx_class = SimpleView


class SparseSheet:
	_hx_class_name = "SparseSheet"
	_hx_fields = ["h", "w", "row", "zero"]
	_hx_methods = ["resize", "nonDestructiveResize", "get", "set"]

	def __init__(self):
		self.h = None
		self.w = None
		self.row = None
		self.zero = None
		def _hx_local_0():
			self.w = 0
			return self.w
		self.h = _hx_local_0()

	def resize(self,w,h,zero):
		self.row = haxe_ds_IntMap()
		self.nonDestructiveResize(w,h,zero)

	def nonDestructiveResize(self,w,h,zero):
		self.w = w
		self.h = h
		self.zero = zero

	def get(self,x,y):
		cursor = self.row.h.get(y,None)
		if (cursor is None):
			return self.zero
		val = cursor.h.get(x,None)
		if (val is None):
			return self.zero
		return val

	def set(self,x,y,val):
		cursor = self.row.h.get(y,None)
		if (cursor is None):
			cursor = haxe_ds_IntMap()
			self.row.set(y,cursor)
		cursor.set(x,val)

SparseSheet._hx_class = SparseSheet


class SqlColumn:
	_hx_class_name = "SqlColumn"
	_hx_fields = ["name", "primary"]
	_hx_methods = ["getName", "isPrimaryKey", "toString"]
	_hx_statics = ["byNameAndPrimaryKey"]

	def __init__(self):
		self.name = None
		self.primary = None

	def getName(self):
		return self.name

	def isPrimaryKey(self):
		return self.primary

	def toString(self):
		return (HxOverrides.stringOrNull((("*" if (self.primary) else ""))) + HxOverrides.stringOrNull(self.name))

	@staticmethod
	def byNameAndPrimaryKey(name,primary):
		result = SqlColumn()
		result.name = name
		result.primary = primary
		return result

SqlColumn._hx_class = SqlColumn


class SqlCompare:
	_hx_class_name = "SqlCompare"
	_hx_fields = ["db", "parent", "local", "remote", "at0", "at1", "align"]
	_hx_methods = ["equalArray", "validateSchema", "denull", "link", "linkQuery", "apply"]

	def __init__(self,db,local,remote):
		self.db = None
		self.parent = None
		self.local = None
		self.remote = None
		self.at0 = None
		self.at1 = None
		self.align = None
		self.db = db
		self.local = local
		self.remote = remote

	def equalArray(self,a1,a2):
		if (len(a1) != len(a2)):
			return False
		_g1 = 0
		_g = len(a1)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if ((a1[i] if i >= 0 and i < len(a1) else None) != (a2[i] if i >= 0 and i < len(a2) else None)):
				return False
		return True

	def validateSchema(self):
		all_cols1 = self.local.getColumnNames()
		all_cols2 = self.remote.getColumnNames()
		if (not self.equalArray(all_cols1,all_cols2)):
			return False
		key_cols1 = self.local.getPrimaryKey()
		key_cols2 = self.remote.getPrimaryKey()
		if (not self.equalArray(key_cols1,key_cols2)):
			return False
		if (len(key_cols1) == 0):
			return False
		return True

	def denull(self,x):
		if (x is None):
			return -1
		return x

	def link(self):
		i0 = self.denull(self.db.get(0))
		i1 = self.denull(self.db.get(1))
		if (i0 == -3):
			i0 = self.at0
			_hx_local_0 = self
			_hx_local_1 = _hx_local_0.at0
			_hx_local_0.at0 = (_hx_local_1 + 1)
			_hx_local_1
		if (i1 == -3):
			i1 = self.at1
			_hx_local_2 = self
			_hx_local_3 = _hx_local_2.at1
			_hx_local_2.at1 = (_hx_local_3 + 1)
			_hx_local_3
		factor = None
		if ((i0 >= 0) and ((i1 >= 0))):
			factor = 2
		else:
			factor = 1
		offset = (factor - 1)
		if (i0 >= 0):
			_g1 = 0
			_g = self.local.get_width()
			while (_g1 < _g):
				x = _g1
				_g1 = (_g1 + 1)
				self.local.setCellCache(x,i0,self.db.get((2 + ((factor * x)))))
		if (i1 >= 0):
			_g11 = 0
			_g2 = self.remote.get_width()
			while (_g11 < _g2):
				x1 = _g11
				_g11 = (_g11 + 1)
				self.remote.setCellCache(x1,i1,self.db.get(((2 + ((factor * x1))) + offset)))
		self.align.link(i0,i1)
		self.align.addToOrder(i0,i1)

	def linkQuery(self,query,order):
		if self.db.begin(query,None,order):
			while self.db.read():
				self.link()
			self.db.end()

	def apply(self):
		if (self.db is None):
			return None
		if (not self.validateSchema()):
			return None
		rowid_name = self.db.rowid()
		self.align = Alignment()
		key_cols = self.local.getPrimaryKey()
		data_cols = self.local.getAllButPrimaryKey()
		all_cols = self.local.getColumnNames()
		self.align.meta = Alignment()
		_g1 = 0
		_g = len(all_cols)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			self.align.meta.link(i,i)
		self.align.meta.range(len(all_cols),len(all_cols))
		self.align.tables(self.local,self.remote)
		self.align.range(999,999)
		sql_table1 = self.local.getQuotedTableName()
		sql_table2 = self.remote.getQuotedTableName()
		sql_key_cols = ""
		_g11 = 0
		_g2 = len(key_cols)
		while (_g11 < _g2):
			i1 = _g11
			_g11 = (_g11 + 1)
			if (i1 > 0):
				sql_key_cols = (("null" if sql_key_cols is None else sql_key_cols) + ",")
			sql_key_cols = (("null" if sql_key_cols is None else sql_key_cols) + HxOverrides.stringOrNull(self.local.getQuotedColumnName((key_cols[i1] if i1 >= 0 and i1 < len(key_cols) else None))))
		sql_all_cols = ""
		_g12 = 0
		_g3 = len(all_cols)
		while (_g12 < _g3):
			i2 = _g12
			_g12 = (_g12 + 1)
			if (i2 > 0):
				sql_all_cols = (("null" if sql_all_cols is None else sql_all_cols) + ",")
			sql_all_cols = (("null" if sql_all_cols is None else sql_all_cols) + HxOverrides.stringOrNull(self.local.getQuotedColumnName((all_cols[i2] if i2 >= 0 and i2 < len(all_cols) else None))))
		sql_key_match = ""
		_g13 = 0
		_g4 = len(key_cols)
		while (_g13 < _g4):
			i3 = _g13
			_g13 = (_g13 + 1)
			if (i3 > 0):
				sql_key_match = (("null" if sql_key_match is None else sql_key_match) + " AND ")
			n = self.local.getQuotedColumnName((key_cols[i3] if i3 >= 0 and i3 < len(key_cols) else None))
			sql_key_match = (("null" if sql_key_match is None else sql_key_match) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n is None else n)) + " IS ") + ("null" if sql_table2 is None else sql_table2)) + ".") + ("null" if n is None else n)))))
		sql_data_mismatch = ""
		_g14 = 0
		_g5 = len(data_cols)
		while (_g14 < _g5):
			i4 = _g14
			_g14 = (_g14 + 1)
			if (i4 > 0):
				sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + " OR ")
			n1 = self.local.getQuotedColumnName((data_cols[i4] if i4 >= 0 and i4 < len(data_cols) else None))
			sql_data_mismatch = (("null" if sql_data_mismatch is None else sql_data_mismatch) + HxOverrides.stringOrNull((((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n1 is None else n1)) + " IS NOT ") + ("null" if sql_table2 is None else sql_table2)) + ".") + ("null" if n1 is None else n1)))))
		sql_dbl_cols = ""
		dbl_cols = []
		_g15 = 0
		_g6 = len(all_cols)
		while (_g15 < _g6):
			i5 = _g15
			_g15 = (_g15 + 1)
			if (i5 > 0):
				sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + ",")
			n2 = self.local.getQuotedColumnName((all_cols[i5] if i5 >= 0 and i5 < len(all_cols) else None))
			buf = ("__coopy_" + Std.string(i5))
			sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + HxOverrides.stringOrNull((((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n2 is None else n2)) + " AS ") + ("null" if buf is None else buf)))))
			dbl_cols.append(buf)
			sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + ",")
			sql_dbl_cols = (("null" if sql_dbl_cols is None else sql_dbl_cols) + HxOverrides.stringOrNull(((((((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if n2 is None else n2)) + " AS ") + ("null" if buf is None else buf)) + "b"))))
			dbl_cols.append((("null" if buf is None else buf) + "b"))
		sql_order = ""
		_g16 = 0
		_g7 = len(key_cols)
		while (_g16 < _g7):
			i6 = _g16
			_g16 = (_g16 + 1)
			if (i6 > 0):
				sql_order = (("null" if sql_order is None else sql_order) + ",")
			n3 = self.local.getQuotedColumnName((key_cols[i6] if i6 >= 0 and i6 < len(key_cols) else None))
			sql_order = (("null" if sql_order is None else sql_order) + ("null" if n3 is None else n3))
		sql_dbl_order = ""
		_g17 = 0
		_g8 = len(key_cols)
		while (_g17 < _g8):
			i7 = _g17
			_g17 = (_g17 + 1)
			if (i7 > 0):
				sql_dbl_order = (("null" if sql_dbl_order is None else sql_dbl_order) + ",")
			n4 = self.local.getQuotedColumnName((key_cols[i7] if i7 >= 0 and i7 < len(key_cols) else None))
			sql_dbl_order = (("null" if sql_dbl_order is None else sql_dbl_order) + HxOverrides.stringOrNull((((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if n4 is None else n4)))))
		rowid = "-3"
		rowid1 = "-3"
		rowid2 = "-3"
		if (rowid_name is not None):
			rowid = rowid_name
			rowid1 = ((("null" if sql_table1 is None else sql_table1) + ".") + ("null" if rowid_name is None else rowid_name))
			rowid2 = ((("null" if sql_table2 is None else sql_table2) + ".") + ("null" if rowid_name is None else rowid_name))
		sql_inserts = (((((((((("SELECT DISTINCT NULL, " + ("null" if rowid is None else rowid)) + " AS rowid, ") + ("null" if sql_all_cols is None else sql_all_cols)) + " FROM ") + ("null" if sql_table2 is None else sql_table2)) + " WHERE NOT EXISTS (SELECT 1 FROM ") + ("null" if sql_table1 is None else sql_table1)) + " WHERE ") + ("null" if sql_key_match is None else sql_key_match)) + ")")
		sql_inserts_order = (["NULL", "rowid"] + all_cols)
		sql_updates = ((((((((((((("SELECT DISTINCT " + ("null" if rowid1 is None else rowid1)) + " AS __coopy_rowid0, ") + ("null" if rowid2 is None else rowid2)) + " AS __coopy_rowid1, ") + ("null" if sql_dbl_cols is None else sql_dbl_cols)) + " FROM ") + ("null" if sql_table1 is None else sql_table1)) + " INNER JOIN ") + ("null" if sql_table2 is None else sql_table2)) + " ON ") + ("null" if sql_key_match is None else sql_key_match)) + " WHERE ") + ("null" if sql_data_mismatch is None else sql_data_mismatch))
		sql_updates_order = (["__coopy_rowid0", "__coopy_rowid1"] + dbl_cols)
		sql_deletes = (((((((((("SELECT DISTINCT " + ("null" if rowid is None else rowid)) + " AS rowid, NULL, ") + ("null" if sql_all_cols is None else sql_all_cols)) + " FROM ") + ("null" if sql_table1 is None else sql_table1)) + " WHERE NOT EXISTS (SELECT 1 FROM ") + ("null" if sql_table2 is None else sql_table2)) + " WHERE ") + ("null" if sql_key_match is None else sql_key_match)) + ")")
		sql_deletes_order = (["rowid", "NULL"] + all_cols)
		self.at0 = 1
		self.at1 = 1
		self.linkQuery(sql_inserts,sql_inserts_order)
		self.linkQuery(sql_updates,sql_updates_order)
		self.linkQuery(sql_deletes,sql_deletes_order)
		return self.align

SqlCompare._hx_class = SqlCompare


class SqlDatabase:
	_hx_class_name = "SqlDatabase"
	_hx_methods = ["getColumns", "getQuotedTableName", "getQuotedColumnName", "begin", "beginRow", "read", "get", "end", "width", "rowid"]
SqlDatabase._hx_class = SqlDatabase


class SqlHelper:
	_hx_class_name = "SqlHelper"
	_hx_methods = ["getTableNames", "countRows", "getRowIDs"]
SqlHelper._hx_class = SqlHelper


class SqlTable:
	_hx_class_name = "SqlTable"
	_hx_fields = ["db", "columns", "name", "quotedTableName", "cache", "columnNames", "h", "helper", "id2rid"]
	_hx_methods = ["getColumns", "getPrimaryKey", "getAllButPrimaryKey", "getColumnNames", "getQuotedTableName", "getQuotedColumnName", "getCell", "setCellCache", "setCell", "getCellView", "isResizable", "resize", "clear", "insertOrDeleteRows", "insertOrDeleteColumns", "trimBlank", "get_width", "get_height", "getData", "clone"]
	_hx_interfaces = [Table]

	def __init__(self,db,name,helper = None):
		self.db = None
		self.columns = None
		self.name = None
		self.quotedTableName = None
		self.cache = None
		self.columnNames = None
		self.h = None
		self.helper = None
		self.id2rid = None
		self.db = db
		self.name = name
		self.helper = helper
		self.cache = haxe_ds_IntMap()
		self.h = -1
		self.id2rid = None
		self.getColumns()

	def getColumns(self):
		if (self.columns is not None):
			return
		if (self.db is None):
			return
		self.columns = self.db.getColumns(self.name)
		self.columnNames = list()
		_g = 0
		_g1 = self.columns
		while (_g < len(_g1)):
			col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			_this = self.columnNames
			x = col.getName()
			_this.append(x)

	def getPrimaryKey(self):
		self.getColumns()
		result = list()
		_g = 0
		_g1 = self.columns
		while (_g < len(_g1)):
			col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if (not col.isPrimaryKey()):
				continue
			x = col.getName()
			result.append(x)
		return result

	def getAllButPrimaryKey(self):
		self.getColumns()
		result = list()
		_g = 0
		_g1 = self.columns
		while (_g < len(_g1)):
			col = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
			_g = (_g + 1)
			if col.isPrimaryKey():
				continue
			x = col.getName()
			result.append(x)
		return result

	def getColumnNames(self):
		self.getColumns()
		return self.columnNames

	def getQuotedTableName(self):
		if (self.quotedTableName is not None):
			return self.quotedTableName
		self.quotedTableName = self.db.getQuotedTableName(self.name)
		return self.quotedTableName

	def getQuotedColumnName(self,name):
		return self.db.getQuotedColumnName(name)

	def getCell(self,x,y):
		if (self.h >= 0):
			y = (y - 1)
			if (y >= 0):
				y = (self.id2rid[y] if y >= 0 and y < len(self.id2rid) else None)
		if (y < 0):
			self.getColumns()
			return (self.columns[x] if x >= 0 and x < len(self.columns) else None).name
		row = self.cache.h.get(y,None)
		if (row is None):
			row = haxe_ds_IntMap()
			self.getColumns()
			self.db.beginRow(self.name,y,self.columnNames)
			while self.db.read():
				_g1 = 0
				_g = self.get_width()
				while (_g1 < _g):
					i = _g1
					_g1 = (_g1 + 1)
					v = self.db.get(i)
					row.set(i,v)
					v
			self.db.end()
			self.cache.set(y,row)
			row
		this1 = self.cache.h.get(y,None)
		return this1.get(x)

	def setCellCache(self,x,y,c):
		row = self.cache.h.get(y,None)
		if (row is None):
			row = haxe_ds_IntMap()
			self.getColumns()
			self.cache.set(y,row)
			row
		v = c
		row.set(x,v)
		v

	def setCell(self,x,y,c):
		print(str("SqlTable cannot set cells yet"))

	def getCellView(self):
		return SimpleView()

	def isResizable(self):
		return False

	def resize(self,w,h):
		return False

	def clear(self):
		pass

	def insertOrDeleteRows(self,fate,hfate):
		return False

	def insertOrDeleteColumns(self,fate,wfate):
		return False

	def trimBlank(self):
		return False

	def get_width(self):
		self.getColumns()
		return len(self.columns)

	def get_height(self):
		if (self.h >= 0):
			return self.h
		if (self.helper is None):
			return -1
		self.id2rid = self.helper.getRowIDs(self.db,self.name)
		self.h = (len(self.id2rid) + 1)
		return self.h

	def getData(self):
		return None

	def clone(self):
		return None

SqlTable._hx_class = SqlTable


class SqlTableName:
	_hx_class_name = "SqlTableName"
	_hx_fields = ["name", "prefix"]
	_hx_methods = ["toString"]

	def __init__(self,name = "",prefix = ""):
		if (name is None):
			name = ""
		if (prefix is None):
			prefix = ""
		self.name = None
		self.prefix = None
		self.name = name
		self.prefix = prefix

	def toString(self):
		if (self.prefix == ""):
			return self.name
		return ((HxOverrides.stringOrNull(self.prefix) + ".") + HxOverrides.stringOrNull(self.name))

SqlTableName._hx_class = SqlTableName


class SqliteHelper:
	_hx_class_name = "SqliteHelper"
	_hx_methods = ["getTableNames", "countRows", "getRowIDs"]
	_hx_interfaces = [SqlHelper]

	def __init__(self):
		pass

	def getTableNames(self,db):
		q = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
		if (not db.begin(q,None,["name"])):
			return None
		names = list()
		while db.read():
			x = db.get(0)
			names.append(x)
		db.end()
		return names

	def countRows(self,db,name):
		q = ("SELECT COUNT(*) AS ct FROM " + HxOverrides.stringOrNull(db.getQuotedTableName(name)))
		if (not db.begin(q,None,["ct"])):
			return -1
		ct = -1
		while db.read():
			ct = db.get(0)
		db.end()
		return ct

	def getRowIDs(self,db,name):
		result = list()
		q = (("SELECT ROWID AS r FROM " + HxOverrides.stringOrNull(db.getQuotedTableName(name))) + " ORDER BY ROWID")
		if (not db.begin(q,None,["r"])):
			return None
		while db.read():
			c = db.get(0)
			result.append(c)
		db.end()
		return result

SqliteHelper._hx_class = SqliteHelper


class Std:
	_hx_class_name = "Std"
	_hx_statics = ["is", "string", "parseInt", "shortenPossibleNumber", "parseFloat"]

	@staticmethod
	def _hx_is(v,t):
		if ((v is None) and ((t is None))):
			return False
		if (t is None):
			return False
		if (t == Dynamic):
			return True
		isBool = isinstance(v,bool)
		if ((t == Bool) and isBool):
			return True
		if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
			return True
		vIsFloat = isinstance(v,float)
		def _hx_local_0():
			f = v
			return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
		def _hx_local_1():
			x = v
			def _hx_local_4():
				def _hx_local_3():
					_hx_local_2 = None
					try:
						_hx_local_2 = int(x)
					except Exception as _hx_e:
						_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
						e = _hx_e1
						_hx_local_2 = None
					return _hx_local_2
				return _hx_local_3()
			return _hx_local_4()
		if (((((((not isBool) and vIsFloat) and (t == Int)) and _hx_local_0()) and ((v == _hx_local_1()))) and ((v <= 2147483647))) and ((v >= -2147483648))):
			return True
		if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
			return True
		if (t == str):
			return isinstance(v,str)
		isEnumType = (t == Enum)
		if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
			return True
		if isEnumType:
			return False
		isClassType = (t == Class)
		if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
			return True
		if isClassType:
			return False
		def _hx_local_6():
			_hx_local_5 = None
			try:
				_hx_local_5 = isinstance(v,t)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				_hx_local_5 = False
			return _hx_local_5
		if _hx_local_6():
			return True
		if python_lib_Inspect.isclass(t):
			loop = None
			loop1 = None
			def _hx_local_8(intf):
				f1 = None
				if hasattr(intf,"_hx_interfaces"):
					f1 = intf._hx_interfaces
				else:
					f1 = []
				if (f1 is not None):
					_g = 0
					while (_g < len(f1)):
						i = (f1[_g] if _g >= 0 and _g < len(f1) else None)
						_g = (_g + 1)
						if HxOverrides.eq(i,t):
							return True
						else:
							l = loop1(i)
							if l:
								return True
					return False
				else:
					return False
			loop1 = _hx_local_8
			loop = loop1
			currentClass = v.__class__
			while (currentClass is not None):
				if loop(currentClass):
					return True
				currentClass = python_Boot.getSuperClass(currentClass)
			return False
		else:
			return False

	@staticmethod
	def string(s):
		return python_Boot.toString1(s,"")

	@staticmethod
	def parseInt(x):
		if (x is None):
			return None
		try:
			return int(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			try:
				prefix = None
				_this = HxString.substr(x,0,2)
				prefix = _this.lower()
				if (prefix == "0x"):
					return int(x,16)
				raise _HxException("fail")
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e1 = _hx_e1
				r = None
				x1 = Std.parseFloat(x)
				try:
					r = int(x1)
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					r = None
				if (r is None):
					r1 = Std.shortenPossibleNumber(x)
					if (r1 != x):
						return Std.parseInt(r1)
					else:
						return None
				return r

	@staticmethod
	def shortenPossibleNumber(x):
		r = ""
		_g1 = 0
		_g = len(x)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			c = None
			if ((i < 0) or ((i >= len(x)))):
				c = ""
			else:
				c = x[i]
			_g2 = HxString.charCodeAt(c,0)
			if (_g2 is not None):
				if (((((((((((_g2 == 46) or ((_g2 == 57))) or ((_g2 == 56))) or ((_g2 == 55))) or ((_g2 == 54))) or ((_g2 == 53))) or ((_g2 == 52))) or ((_g2 == 51))) or ((_g2 == 50))) or ((_g2 == 49))) or ((_g2 == 48))):
					r = (("null" if r is None else r) + ("null" if c is None else c))
				else:
					break
			else:
				break
		return r

	@staticmethod
	def parseFloat(x):
		try:
			return float(x)
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e = _hx_e1
			if (x is not None):
				r1 = Std.shortenPossibleNumber(x)
				if (r1 != x):
					return Std.parseFloat(r1)
			return Math.NaN
Std._hx_class = Std


class Float:
	_hx_class_name = "Float"
Float._hx_class = Float


class Int:
	_hx_class_name = "Int"
Int._hx_class = Int


class Bool:
	_hx_class_name = "Bool"
Bool._hx_class = Bool


class Dynamic:
	_hx_class_name = "Dynamic"
Dynamic._hx_class = Dynamic


class StringBuf:
	_hx_class_name = "StringBuf"
	_hx_fields = ["b"]

	def __init__(self):
		self.b = None
		self.b = python_lib_io_StringIO()

StringBuf._hx_class = StringBuf


class StringTools:
	_hx_class_name = "StringTools"
	_hx_statics = ["lpad", "replace"]

	@staticmethod
	def lpad(s,c,l):
		if (len(c) <= 0):
			return s
		while (len(s) < l):
			s = (("null" if c is None else c) + ("null" if s is None else s))
		return s

	@staticmethod
	def replace(s,sub,by):
		_this = None
		if (sub == ""):
			_this = list(s)
		else:
			_this = s.split(sub)
		return by.join([python_Boot.toString1(x1,'') for x1 in _this])
StringTools._hx_class = StringTools


class TableComparisonState:
	_hx_class_name = "TableComparisonState"
	_hx_fields = ["p", "a", "b", "completed", "run_to_completion", "is_equal", "is_equal_known", "has_same_columns", "has_same_columns_known", "compare_flags"]
	_hx_methods = ["reset"]

	def __init__(self):
		self.p = None
		self.a = None
		self.b = None
		self.completed = None
		self.run_to_completion = None
		self.is_equal = None
		self.is_equal_known = None
		self.has_same_columns = None
		self.has_same_columns_known = None
		self.compare_flags = None
		self.reset()

	def reset(self):
		self.completed = False
		self.run_to_completion = True
		self.is_equal_known = False
		self.is_equal = False
		self.has_same_columns = False
		self.has_same_columns_known = False
		self.compare_flags = None

TableComparisonState._hx_class = TableComparisonState


class TableDiff:
	_hx_class_name = "TableDiff"
	_hx_fields = ["align", "flags", "builder"]
	_hx_methods = ["setCellBuilder", "getSeparator", "quoteForDiff", "isReordered", "spreadContext", "setIgnore", "countActive", "hilite"]

	def __init__(self,align,flags):
		self.align = None
		self.flags = None
		self.builder = None
		self.align = align
		self.flags = flags
		self.builder = None

	def setCellBuilder(self,builder):
		self.builder = builder

	def getSeparator(self,t,t2,root):
		sep = root
		w = t.get_width()
		h = t.get_height()
		view = t.getCellView()
		_g = 0
		while (_g < h):
			y = _g
			_g = (_g + 1)
			_g1 = 0
			while (_g1 < w):
				x = _g1
				_g1 = (_g1 + 1)
				txt = view.toString(t.getCell(x,y))
				if (txt is None):
					continue
				while (txt.find(sep) >= 0):
					sep = ("-" + ("null" if sep is None else sep))
		if (t2 is not None):
			w = t2.get_width()
			h = t2.get_height()
			_g2 = 0
			while (_g2 < h):
				y1 = _g2
				_g2 = (_g2 + 1)
				_g11 = 0
				while (_g11 < w):
					x1 = _g11
					_g11 = (_g11 + 1)
					txt1 = view.toString(t2.getCell(x1,y1))
					if (txt1 is None):
						continue
					while (txt1.find(sep) >= 0):
						sep = ("-" + ("null" if sep is None else sep))
		return sep

	def quoteForDiff(self,v,d):
		nil = "NULL"
		if v.equals(d,None):
			return nil
		_hx_str = v.toString(d)
		score = 0
		_g1 = 0
		_g = len(_hx_str)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if (HxString.charCodeAt(_hx_str,score) != 95):
				break
			score = (score + 1)
		if (HxString.substr(_hx_str,score,None) == nil):
			_hx_str = ("_" + ("null" if _hx_str is None else _hx_str))
		return _hx_str

	def isReordered(self,m,ct):
		reordered = False
		l = -1
		r = -1
		_g = 0
		while (_g < ct):
			i = _g
			_g = (_g + 1)
			unit = m.h.get(i,None)
			if (unit is None):
				continue
			if (unit.l >= 0):
				if (unit.l < l):
					reordered = True
					break
				l = unit.l
			if (unit.r >= 0):
				if (unit.r < r):
					reordered = True
					break
				r = unit.r
		return reordered

	def spreadContext(self,units,_hx_del,active):
		if ((_hx_del > 0) and ((active is not None))):
			mark = (-_hx_del - 1)
			skips = 0
			_g1 = 0
			_g = len(units)
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				if ((active[i] if i >= 0 and i < len(active) else None) == -3):
					skips = (skips + 1)
					continue
				if (((active[i] if i >= 0 and i < len(active) else None) == 0) or (((active[i] if i >= 0 and i < len(active) else None) == 3))):
					if ((i - mark) <= ((_hx_del + skips))):
						python_internal_ArrayImpl._set(active, i, 2)
					elif ((i - mark) == (((_hx_del + 1) + skips))):
						python_internal_ArrayImpl._set(active, i, 3)
				elif ((active[i] if i >= 0 and i < len(active) else None) == 1):
					mark = i
					skips = 0
			mark = ((len(units) + _hx_del) + 1)
			skips = 0
			_g11 = 0
			_g2 = len(units)
			while (_g11 < _g2):
				j = _g11
				_g11 = (_g11 + 1)
				i1 = ((len(units) - 1) - j)
				if ((active[i1] if i1 >= 0 and i1 < len(active) else None) == -3):
					skips = (skips + 1)
					continue
				if (((active[i1] if i1 >= 0 and i1 < len(active) else None) == 0) or (((active[i1] if i1 >= 0 and i1 < len(active) else None) == 3))):
					if ((mark - i1) <= ((_hx_del + skips))):
						python_internal_ArrayImpl._set(active, i1, 2)
					elif ((mark - i1) == (((_hx_del + 1) + skips))):
						python_internal_ArrayImpl._set(active, i1, 3)
				elif ((active[i1] if i1 >= 0 and i1 < len(active) else None) == 1):
					mark = i1
					skips = 0

	def setIgnore(self,ignore,idx_ignore,tab,r_header):
		v = tab.getCellView()
		if (tab.get_height() >= r_header):
			_g1 = 0
			_g = tab.get_width()
			while (_g1 < _g):
				i = _g1
				_g1 = (_g1 + 1)
				name = v.toString(tab.getCell(i,r_header))
				if (not name in ignore.h):
					continue
				idx_ignore.set(i,True)

	def countActive(self,active):
		ct = 0
		showed_dummy = False
		_g1 = 0
		_g = len(active)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			publish = ((active[i] if i >= 0 and i < len(active) else None) > 0)
			dummy = ((active[i] if i >= 0 and i < len(active) else None) == 3)
			if (dummy and showed_dummy):
				continue
			if (not publish):
				continue
			showed_dummy = dummy
			ct = (ct + 1)
		return ct

	def hilite(self,output):
		if (not output.isResizable()):
			return False
		if (self.builder is None):
			if self.flags.allow_nested_cells:
				self.builder = NestedCellBuilder()
			else:
				self.builder = FlatCellBuilder()
		output.resize(0,0)
		output.clear()
		row_map = haxe_ds_IntMap()
		col_map = haxe_ds_IntMap()
		order = self.align.toOrder()
		units = order.getList()
		has_parent = (self.align.reference is not None)
		a = None
		b = None
		p = None
		rp_header = 0
		ra_header = 0
		rb_header = 0
		is_index_p = haxe_ds_IntMap()
		is_index_a = haxe_ds_IntMap()
		is_index_b = haxe_ds_IntMap()
		if has_parent:
			p = self.align.getSource()
			a = self.align.reference.getTarget()
			b = self.align.getTarget()
			rp_header = self.align.reference.meta.getSourceHeader()
			ra_header = self.align.reference.meta.getTargetHeader()
			rb_header = self.align.meta.getTargetHeader()
			if (self.align.getIndexColumns() is not None):
				_g = 0
				_g1 = self.align.getIndexColumns()
				while (_g < len(_g1)):
					p2b = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
					_g = (_g + 1)
					if (p2b.l >= 0):
						is_index_p.set(p2b.l,True)
					if (p2b.r >= 0):
						is_index_b.set(p2b.r,True)
			if (self.align.reference.getIndexColumns() is not None):
				_g2 = 0
				_g11 = self.align.reference.getIndexColumns()
				while (_g2 < len(_g11)):
					p2a = (_g11[_g2] if _g2 >= 0 and _g2 < len(_g11) else None)
					_g2 = (_g2 + 1)
					if (p2a.l >= 0):
						is_index_p.set(p2a.l,True)
					if (p2a.r >= 0):
						is_index_a.set(p2a.r,True)
		else:
			a = self.align.getSource()
			b = self.align.getTarget()
			p = a
			ra_header = self.align.meta.getSourceHeader()
			rp_header = ra_header
			rb_header = self.align.meta.getTargetHeader()
			if (self.align.getIndexColumns() is not None):
				_g3 = 0
				_g12 = self.align.getIndexColumns()
				while (_g3 < len(_g12)):
					a2b = (_g12[_g3] if _g3 >= 0 and _g3 < len(_g12) else None)
					_g3 = (_g3 + 1)
					if (a2b.l >= 0):
						is_index_a.set(a2b.l,True)
					if (a2b.r >= 0):
						is_index_b.set(a2b.r,True)
		column_order = self.align.meta.toOrder()
		column_units = column_order.getList()
		p_ignore = haxe_ds_IntMap()
		a_ignore = haxe_ds_IntMap()
		b_ignore = haxe_ds_IntMap()
		ignore = self.flags.getIgnoredColumns()
		if (ignore is not None):
			self.setIgnore(ignore,p_ignore,p,rp_header)
			self.setIgnore(ignore,a_ignore,a,ra_header)
			self.setIgnore(ignore,b_ignore,b,rb_header)
			ncolumn_units = list()
			_g13 = 0
			_g4 = len(column_units)
			while (_g13 < _g4):
				j = _g13
				_g13 = (_g13 + 1)
				cunit = (column_units[j] if j >= 0 and j < len(column_units) else None)
				if ((cunit.p in p_ignore.h or cunit.l in a_ignore.h) or cunit.r in b_ignore.h):
					continue
				ncolumn_units.append(cunit)
			column_units = ncolumn_units
		show_rc_numbers = False
		row_moves = None
		col_moves = None
		if self.flags.ordered:
			row_moves = haxe_ds_IntMap()
			moves = Mover.moveUnits(units)
			_g14 = 0
			_g5 = len(moves)
			while (_g14 < _g5):
				i = _g14
				_g14 = (_g14 + 1)
				row_moves.set((moves[i] if i >= 0 and i < len(moves) else None),i)
				i
			col_moves = haxe_ds_IntMap()
			moves = Mover.moveUnits(column_units)
			_g15 = 0
			_g6 = len(moves)
			while (_g15 < _g6):
				i1 = _g15
				_g15 = (_g15 + 1)
				col_moves.set((moves[i1] if i1 >= 0 and i1 < len(moves) else None),i1)
				i1
		active = list()
		active_column = None
		if (not self.flags.show_unchanged):
			_g16 = 0
			_g7 = len(units)
			while (_g16 < _g7):
				i2 = _g16
				_g16 = (_g16 + 1)
				python_internal_ArrayImpl._set(active, ((len(units) - 1) - i2), 0)
		allow_insert = self.flags.allowInsert()
		allow_delete = self.flags.allowDelete()
		allow_update = self.flags.allowUpdate()
		if (not self.flags.show_unchanged_columns):
			active_column = list()
			_g17 = 0
			_g8 = len(column_units)
			while (_g17 < _g8):
				i3 = _g17
				_g17 = (_g17 + 1)
				v = 0
				unit = (column_units[i3] if i3 >= 0 and i3 < len(column_units) else None)
				if ((unit.l >= 0) and is_index_a.h.get(unit.l,None)):
					v = 1
				if ((unit.r >= 0) and is_index_b.h.get(unit.r,None)):
					v = 1
				if ((unit.p >= 0) and is_index_p.h.get(unit.p,None)):
					v = 1
				python_internal_ArrayImpl._set(active_column, i3, v)
		v1 = a.getCellView()
		self.builder.setView(v1)
		outer_reps_needed = None
		if (self.flags.show_unchanged and self.flags.show_unchanged_columns):
			outer_reps_needed = 1
		else:
			outer_reps_needed = 2
		sep = ""
		conflict_sep = ""
		schema = list()
		have_schema = False
		_g18 = 0
		_g9 = len(column_units)
		while (_g18 < _g9):
			j1 = _g18
			_g18 = (_g18 + 1)
			cunit1 = (column_units[j1] if j1 >= 0 and j1 < len(column_units) else None)
			reordered = False
			if self.flags.ordered:
				if j1 in col_moves.h:
					reordered = True
				if reordered:
					show_rc_numbers = True
			act = ""
			if ((cunit1.r >= 0) and ((cunit1.lp() == -1))):
				have_schema = True
				act = "+++"
				if (active_column is not None):
					if allow_update:
						python_internal_ArrayImpl._set(active_column, j1, 1)
			if ((cunit1.r < 0) and ((cunit1.lp() >= 0))):
				have_schema = True
				act = "---"
				if (active_column is not None):
					if allow_update:
						python_internal_ArrayImpl._set(active_column, j1, 1)
			if ((cunit1.r >= 0) and ((cunit1.lp() >= 0))):
				if ((p.get_height() >= rp_header) and ((b.get_height() >= rb_header))):
					pp = p.getCell(cunit1.lp(),rp_header)
					bb = b.getCell(cunit1.r,rb_header)
					if (not v1.equals(pp,bb)):
						have_schema = True
						act = "("
						act = (("null" if act is None else act) + HxOverrides.stringOrNull(v1.toString(pp)))
						act = (("null" if act is None else act) + ")")
						if (active_column is not None):
							python_internal_ArrayImpl._set(active_column, j1, 1)
			if reordered:
				act = (":" + ("null" if act is None else act))
				have_schema = True
				if (active_column is not None):
					active_column = None
			schema.append(act)
		if have_schema:
			at = output.get_height()
			output.resize((len(column_units) + 1),(at + 1))
			output.setCell(0,at,self.builder.marker("!"))
			_g19 = 0
			_g10 = len(column_units)
			while (_g19 < _g10):
				j2 = _g19
				_g19 = (_g19 + 1)
				output.setCell((j2 + 1),at,v1.toDatum((schema[j2] if j2 >= 0 and j2 < len(schema) else None)))
		top_line_done = False
		if self.flags.always_show_header:
			at1 = output.get_height()
			output.resize((len(column_units) + 1),(at1 + 1))
			output.setCell(0,at1,self.builder.marker("@@"))
			_g110 = 0
			_g20 = len(column_units)
			while (_g110 < _g20):
				j3 = _g110
				_g110 = (_g110 + 1)
				cunit2 = (column_units[j3] if j3 >= 0 and j3 < len(column_units) else None)
				if (cunit2.r >= 0):
					if (b.get_height() != 0):
						output.setCell((j3 + 1),at1,b.getCell(cunit2.r,rb_header))
				elif (cunit2.lp() >= 0):
					if (p.get_height() != 0):
						output.setCell((j3 + 1),at1,p.getCell(cunit2.lp(),rp_header))
				col_map.set((j3 + 1),cunit2)
			top_line_done = True
		output_height = output.get_height()
		output_height_init = output.get_height()
		_g21 = 0
		while (_g21 < outer_reps_needed):
			out = _g21
			_g21 = (_g21 + 1)
			if (out == 1):
				self.spreadContext(units,self.flags.unchanged_context,active)
				self.spreadContext(column_units,self.flags.unchanged_column_context,active_column)
				if (active_column is not None):
					_g22 = 0
					_g111 = len(column_units)
					while (_g22 < _g111):
						i4 = _g22
						_g22 = (_g22 + 1)
						if ((active_column[i4] if i4 >= 0 and i4 < len(active_column) else None) == 3):
							python_internal_ArrayImpl._set(active_column, i4, 0)
				rows = (self.countActive(active) + output_height_init)
				if top_line_done:
					rows = (rows - 1)
				output_height = output_height_init
				if (rows > output.get_height()):
					output.resize((len(column_units) + 1),rows)
			showed_dummy = False
			l = -1
			r = -1
			_g23 = 0
			_g112 = len(units)
			while (_g23 < _g112):
				i5 = _g23
				_g23 = (_g23 + 1)
				unit1 = (units[i5] if i5 >= 0 and i5 < len(units) else None)
				reordered1 = False
				if self.flags.ordered:
					if i5 in row_moves.h:
						reordered1 = True
					if reordered1:
						show_rc_numbers = True
				if ((unit1.r < 0) and ((unit1.l < 0))):
					continue
				if (((unit1.r == 0) and ((unit1.lp() == 0))) and top_line_done):
					continue
				act1 = ""
				if reordered1:
					act1 = ":"
				publish = self.flags.show_unchanged
				dummy = False
				if (out == 1):
					publish = ((active[i5] if i5 >= 0 and i5 < len(active) else None) > 0)
					dummy = ((active[i5] if i5 >= 0 and i5 < len(active) else None) == 3)
					if (dummy and showed_dummy):
						continue
					if (not publish):
						continue
				if (not dummy):
					showed_dummy = False
				at2 = output_height
				if publish:
					output_height = (output_height + 1)
					if (output.get_height() < output_height):
						output.resize((len(column_units) + 1),output_height)
				if dummy:
					_g41 = 0
					_g31 = (len(column_units) + 1)
					while (_g41 < _g31):
						j4 = _g41
						_g41 = (_g41 + 1)
						output.setCell(j4,at2,v1.toDatum("..."))
					showed_dummy = True
					continue
				have_addition = False
				skip = False
				if (((unit1.p < 0) and ((unit1.l < 0))) and ((unit1.r >= 0))):
					if (not allow_insert):
						skip = True
					act1 = "+++"
				if (((((unit1.p >= 0) or (not has_parent))) and ((unit1.l >= 0))) and ((unit1.r < 0))):
					if (not allow_delete):
						skip = True
					act1 = "---"
				if skip:
					if (not publish):
						if (active is not None):
							python_internal_ArrayImpl._set(active, i5, -3)
					continue
				_g42 = 0
				_g32 = len(column_units)
				while (_g42 < _g32):
					j5 = _g42
					_g42 = (_g42 + 1)
					cunit3 = (column_units[j5] if j5 >= 0 and j5 < len(column_units) else None)
					pp1 = None
					ll = None
					rr = None
					dd = None
					dd_to = None
					have_dd_to = False
					dd_to_alt = None
					have_dd_to_alt = False
					have_pp = False
					have_ll = False
					have_rr = False
					if ((cunit3.p >= 0) and ((unit1.p >= 0))):
						pp1 = p.getCell(cunit3.p,unit1.p)
						have_pp = True
					if ((cunit3.l >= 0) and ((unit1.l >= 0))):
						ll = a.getCell(cunit3.l,unit1.l)
						have_ll = True
					if ((cunit3.r >= 0) and ((unit1.r >= 0))):
						rr = b.getCell(cunit3.r,unit1.r)
						have_rr = True
						if (((cunit3.p if have_pp else cunit3.l)) < 0):
							if (rr is not None):
								if (v1.toString(rr) != ""):
									if self.flags.allowUpdate():
										have_addition = True
					if have_pp:
						if (not have_rr):
							dd = pp1
						elif v1.equals(pp1,rr):
							dd = pp1
						else:
							dd = pp1
							dd_to = rr
							have_dd_to = True
							if (not v1.equals(pp1,ll)):
								if (not v1.equals(pp1,rr)):
									dd_to_alt = ll
									have_dd_to_alt = True
					elif have_ll:
						if (not have_rr):
							dd = ll
						elif v1.equals(ll,rr):
							dd = ll
						else:
							dd = ll
							dd_to = rr
							have_dd_to = True
					else:
						dd = rr
					cell = dd
					if (have_dd_to and allow_update):
						if (active_column is not None):
							python_internal_ArrayImpl._set(active_column, j5, 1)
						if (sep == ""):
							if self.builder.needSeparator():
								sep = self.getSeparator(a,b,"->")
								self.builder.setSeparator(sep)
							else:
								sep = "->"
						is_conflict = False
						if have_dd_to_alt:
							if (not v1.equals(dd_to,dd_to_alt)):
								is_conflict = True
						if (not is_conflict):
							cell = self.builder.update(dd,dd_to)
							if (len(sep) > len(act1)):
								act1 = sep
						else:
							if (conflict_sep == ""):
								if self.builder.needSeparator():
									conflict_sep = (HxOverrides.stringOrNull(self.getSeparator(p,a,"!")) + ("null" if sep is None else sep))
									self.builder.setConflictSeparator(conflict_sep)
								else:
									conflict_sep = "!->"
							cell = self.builder.conflict(dd,dd_to_alt,dd_to)
							act1 = conflict_sep
					if ((act1 == "") and have_addition):
						act1 = "+"
					if (act1 == "+++"):
						if have_rr:
							if (active_column is not None):
								python_internal_ArrayImpl._set(active_column, j5, 1)
					if publish:
						if ((active_column is None) or (((active_column[j5] if j5 >= 0 and j5 < len(active_column) else None) > 0))):
							output.setCell((j5 + 1),at2,cell)
				if publish:
					output.setCell(0,at2,self.builder.marker(act1))
					row_map.set(at2,unit1)
				if (act1 != ""):
					if (not publish):
						if (active is not None):
							python_internal_ArrayImpl._set(active, i5, 1)
		if (not show_rc_numbers):
			if self.flags.always_show_order:
				show_rc_numbers = True
			elif self.flags.ordered:
				show_rc_numbers = self.isReordered(row_map,output.get_height())
				if (not show_rc_numbers):
					show_rc_numbers = self.isReordered(col_map,output.get_width())
		admin_w = 1
		if (show_rc_numbers and (not self.flags.never_show_order)):
			admin_w = (admin_w + 1)
			target = list()
			_g113 = 0
			_g24 = output.get_width()
			while (_g113 < _g24):
				i6 = _g113
				_g113 = (_g113 + 1)
				target.append((i6 + 1))
			output.insertOrDeleteColumns(target,(output.get_width() + 1))
			_g114 = 0
			_g25 = output.get_height()
			while (_g114 < _g25):
				i7 = _g114
				_g114 = (_g114 + 1)
				unit2 = row_map.h.get(i7,None)
				if (unit2 is None):
					output.setCell(0,i7,"")
					continue
				output.setCell(0,i7,self.builder.links(unit2))
			target = list()
			_g115 = 0
			_g26 = output.get_height()
			while (_g115 < _g26):
				i8 = _g115
				_g115 = (_g115 + 1)
				target.append((i8 + 1))
			output.insertOrDeleteRows(target,(output.get_height() + 1))
			_g116 = 1
			_g27 = output.get_width()
			while (_g116 < _g27):
				i9 = _g116
				_g116 = (_g116 + 1)
				unit3 = col_map.h.get((i9 - 1),None)
				if (unit3 is None):
					output.setCell(i9,0,"")
					continue
				output.setCell(i9,0,self.builder.links(unit3))
			output.setCell(0,0,self.builder.marker("@:@"))
		if (active_column is not None):
			all_active = True
			_g117 = 0
			_g28 = len(active_column)
			while (_g117 < _g28):
				i10 = _g117
				_g117 = (_g117 + 1)
				if ((active_column[i10] if i10 >= 0 and i10 < len(active_column) else None) == 0):
					all_active = False
					break
			if (not all_active):
				fate = list()
				_g29 = 0
				while (_g29 < admin_w):
					i11 = _g29
					_g29 = (_g29 + 1)
					fate.append(i11)
				at3 = admin_w
				ct = 0
				dots = list()
				_g118 = 0
				_g30 = len(active_column)
				while (_g118 < _g30):
					i12 = _g118
					_g118 = (_g118 + 1)
					off = ((active_column[i12] if i12 >= 0 and i12 < len(active_column) else None) == 0)
					if off:
						ct = (ct + 1)
					else:
						ct = 0
					if (off and ((ct > 1))):
						fate.append(-1)
					else:
						if off:
							dots.append(at3)
						fate.append(at3)
						at3 = (at3 + 1)
				output.insertOrDeleteColumns(fate,at3)
				_g33 = 0
				while (_g33 < len(dots)):
					d = (dots[_g33] if _g33 >= 0 and _g33 < len(dots) else None)
					_g33 = (_g33 + 1)
					_g210 = 0
					_g119 = output.get_height()
					while (_g210 < _g119):
						j6 = _g210
						_g210 = (_g210 + 1)
						output.setCell(d,j6,self.builder.marker("..."))
		return True

TableDiff._hx_class = TableDiff


class TableIO:
	_hx_class_name = "TableIO"
	_hx_methods = ["getContent", "saveContent", "args", "writeStdout", "writeStderr", "command", "async", "exists", "openSqliteDatabase"]

	def __init__(self):
		pass

	def getContent(self,name):
		return ""

	def saveContent(self,name,txt):
		return False

	def args(self):
		return []

	def writeStdout(self,txt):
		pass

	def writeStderr(self,txt):
		pass

	def command(self,cmd,args):
		return 1

	def async(self):
		return False

	def exists(self,path):
		return False

	def openSqliteDatabase(self,path):
		return None

TableIO._hx_class = TableIO


class TableModifier:
	_hx_class_name = "TableModifier"
	_hx_fields = ["t"]
	_hx_methods = ["removeColumn"]

	def __init__(self,t):
		self.t = None
		self.t = t

	def removeColumn(self,at):
		fate = []
		_g1 = 0
		_g = self.t.get_width()
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if (i < at):
				fate.append(i)
			elif (i > at):
				fate.append((i - 1))
			else:
				fate.append(-1)
		return self.t.insertOrDeleteColumns(fate,(self.t.get_width() - 1))

TableModifier._hx_class = TableModifier


class TerminalDiffRender:
	_hx_class_name = "TerminalDiffRender"
	_hx_fields = ["codes", "t", "csv", "v", "align_columns"]
	_hx_methods = ["alignColumns", "render", "getText", "pickSizes"]

	def __init__(self):
		self.codes = None
		self.t = None
		self.csv = None
		self.v = None
		self.align_columns = None
		self.align_columns = True

	def alignColumns(self,enable):
		self.align_columns = enable

	def render(self,t):
		self.csv = Csv()
		result = ""
		w = t.get_width()
		h = t.get_height()
		txt = ""
		self.t = t
		self.v = t.getCellView()
		self.codes = haxe_ds_StringMap()
		self.codes.h["header"] = "\x1B[0;1m"
		self.codes.h["spec"] = "\x1B[35;1m"
		self.codes.h["add"] = "\x1B[32;1m"
		self.codes.h["conflict"] = "\x1B[33;1m"
		self.codes.h["modify"] = "\x1B[34;1m"
		self.codes.h["remove"] = "\x1B[31;1m"
		self.codes.h["minor"] = "\x1B[2m"
		self.codes.h["done"] = "\x1B[0m"
		sizes = None
		if self.align_columns:
			sizes = self.pickSizes(t)
		_g = 0
		while (_g < h):
			y = _g
			_g = (_g + 1)
			_g1 = 0
			while (_g1 < w):
				x = _g1
				_g1 = (_g1 + 1)
				if (x > 0):
					txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull((((HxOverrides.stringOrNull(self.codes.h.get("minor",None)) + ",") + HxOverrides.stringOrNull(self.codes.h.get("done",None))))))
				txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(self.getText(x,y,True)))
				if (sizes is not None):
					bit = self.getText(x,y,False)
					_g3 = 0
					_g2 = ((sizes[x] if x >= 0 and x < len(sizes) else None) - len(bit))
					while (_g3 < _g2):
						i = _g3
						_g3 = (_g3 + 1)
						txt = (("null" if txt is None else txt) + " ")
			txt = (("null" if txt is None else txt) + "\r\n")
		self.t = None
		self.v = None
		self.csv = None
		self.codes = None
		return txt

	def getText(self,x,y,color):
		val = self.t.getCell(x,y)
		cell = DiffRender.renderCell(self.t,self.v,x,y)
		if color:
			code = None
			if (cell.category is not None):
				code = self.codes.h.get(cell.category,None)
			if (cell.category_given_tr is not None):
				code_tr = self.codes.h.get(cell.category_given_tr,None)
				if (code_tr is not None):
					code = code_tr
			if (code is not None):
				if (cell.rvalue is not None):
					val = ((((((HxOverrides.stringOrNull(self.codes.h.get("remove",None)) + HxOverrides.stringOrNull(cell.lvalue)) + HxOverrides.stringOrNull(self.codes.h.get("modify",None))) + HxOverrides.stringOrNull(cell.pretty_separator)) + HxOverrides.stringOrNull(self.codes.h.get("add",None))) + HxOverrides.stringOrNull(cell.rvalue)) + HxOverrides.stringOrNull(self.codes.h.get("done",None)))
					if (cell.pvalue is not None):
						val = ((((HxOverrides.stringOrNull(self.codes.h.get("conflict",None)) + HxOverrides.stringOrNull(cell.pvalue)) + HxOverrides.stringOrNull(self.codes.h.get("modify",None))) + HxOverrides.stringOrNull(cell.pretty_separator)) + Std.string(val))
				else:
					val = cell.pretty_value
					val = ((("null" if code is None else code) + Std.string(val)) + HxOverrides.stringOrNull(self.codes.h.get("done",None)))
		else:
			val = cell.pretty_value
		return self.csv.renderCell(self.v,val)

	def pickSizes(self,t):
		w = t.get_width()
		h = t.get_height()
		v = t.getCellView()
		csv = Csv()
		sizes = list()
		row = -1
		total = (w - 1)
		_g = 0
		while (_g < w):
			x = _g
			_g = (_g + 1)
			m = 0
			m2 = 0
			mmax = 0
			mmostmax = 0
			mmin = -1
			_g1 = 0
			while (_g1 < h):
				y = _g1
				_g1 = (_g1 + 1)
				txt = self.getText(x,y,False)
				if ((txt == "@@") and ((row == -1))):
					row = y
				_hx_len = len(txt)
				if (y == row):
					mmin = _hx_len
				m = (m + _hx_len)
				m2 = (m2 + ((_hx_len * _hx_len)))
				if (_hx_len > mmax):
					mmax = _hx_len
			mean = (m / h)
			stddev = None
			v1 = ((m2 / h) - ((mean * mean)))
			if (v1 < 0):
				stddev = Math.NaN
			else:
				stddev = python_lib_Math.sqrt(v1)
			most = None
			def _hx_local_3():
				_hx_local_2 = None
				try:
					_hx_local_2 = int(((mean + ((stddev * 2))) + 0.5))
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e = _hx_e1
					_hx_local_2 = None
				return _hx_local_2
			most = _hx_local_3()
			_g11 = 0
			while (_g11 < h):
				y1 = _g11
				_g11 = (_g11 + 1)
				txt1 = self.getText(x,y1,False)
				len1 = len(txt1)
				if (len1 <= most):
					if (len1 > mmostmax):
						mmostmax = len1
			full = mmax
			most = mmostmax
			if (mmin != -1):
				if (most < mmin):
					most = mmin
			sizes.append(most)
			total = (total + most)
		if (total > 130):
			return None
		return sizes

TerminalDiffRender._hx_class = TerminalDiffRender

class ValueType(Enum):
	_hx_class_name = "ValueType"
	_hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

	@staticmethod
	def TClass(c):
		return ValueType("TClass", 6, [c])

	@staticmethod
	def TEnum(e):
		return ValueType("TEnum", 7, [e])
ValueType.TNull = ValueType("TNull", 0, list())
ValueType.TInt = ValueType("TInt", 1, list())
ValueType.TFloat = ValueType("TFloat", 2, list())
ValueType.TBool = ValueType("TBool", 3, list())
ValueType.TObject = ValueType("TObject", 4, list())
ValueType.TFunction = ValueType("TFunction", 5, list())
ValueType.TUnknown = ValueType("TUnknown", 8, list())
ValueType._hx_class = ValueType


class Type:
	_hx_class_name = "Type"
	_hx_statics = ["typeof"]

	@staticmethod
	def typeof(v):
		if (v is None):
			return ValueType.TNull
		elif isinstance(v,bool):
			return ValueType.TBool
		elif isinstance(v,int):
			return ValueType.TInt
		elif isinstance(v,float):
			return ValueType.TFloat
		elif isinstance(v,str):
			return ValueType.TClass(str)
		elif isinstance(v,list):
			return ValueType.TClass(list)
		elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
			return ValueType.TObject
		elif isinstance(v,Enum):
			return ValueType.TEnum(v.__class__)
		elif (isinstance(v,type) or hasattr(v,"_hx_class")):
			return ValueType.TClass(v.__class__)
		elif callable(v):
			return ValueType.TFunction
		else:
			return ValueType.TUnknown
Type._hx_class = Type


class Unit:
	_hx_class_name = "Unit"
	_hx_fields = ["l", "r", "p"]
	_hx_methods = ["lp", "toString", "fromString"]
	_hx_statics = ["describe"]

	def __init__(self,l = -2,r = -2,p = -2):
		if (l is None):
			l = -2
		if (r is None):
			r = -2
		if (p is None):
			p = -2
		self.l = None
		self.r = None
		self.p = None
		self.l = l
		self.r = r
		self.p = p

	def lp(self):
		if (self.p == -2):
			return self.l
		else:
			return self.p

	def toString(self):
		if (self.p >= -1):
			return ((((HxOverrides.stringOrNull(Unit.describe(self.p)) + "|") + HxOverrides.stringOrNull(Unit.describe(self.l))) + ":") + HxOverrides.stringOrNull(Unit.describe(self.r)))
		return ((HxOverrides.stringOrNull(Unit.describe(self.l)) + ":") + HxOverrides.stringOrNull(Unit.describe(self.r)))

	def fromString(self,txt):
		txt = (("null" if txt is None else txt) + "]")
		at = 0
		_g1 = 0
		_g = len(txt)
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			ch = HxString.charCodeAt(txt,i)
			if ((ch >= 48) and ((ch <= 57))):
				at = (at * 10)
				at = (at + ((ch - 48)))
			elif (ch == 45):
				at = -1
			elif (ch == 124):
				self.p = at
				at = 0
			elif (ch == 58):
				self.l = at
				at = 0
			elif (ch == 93):
				self.r = at
				return True
		return False

	@staticmethod
	def describe(i):
		if (i >= 0):
			return ("" + Std.string(i))
		else:
			return "-"

Unit._hx_class = Unit


class Viterbi:
	_hx_class_name = "Viterbi"
	_hx_fields = ["K", "T", "index", "mode", "path_valid", "best_cost", "cost", "src", "path"]
	_hx_methods = ["reset", "setSize", "assertMode", "addTransition", "endTransitions", "beginTransitions", "calculatePath", "toString", "length", "get", "getCost"]

	def __init__(self):
		self.K = None
		self.T = None
		self.index = None
		self.mode = None
		self.path_valid = None
		self.best_cost = None
		self.cost = None
		self.src = None
		self.path = None
		def _hx_local_0():
			self.T = 0
			return self.T
		self.K = _hx_local_0()
		self.reset()
		self.cost = SparseSheet()
		self.src = SparseSheet()
		self.path = SparseSheet()

	def reset(self):
		self.index = 0
		self.mode = 0
		self.path_valid = False
		self.best_cost = 0

	def setSize(self,states,sequence_length):
		self.K = states
		self.T = sequence_length
		self.cost.resize(self.K,self.T,0)
		self.src.resize(self.K,self.T,-1)
		self.path.resize(1,self.T,-1)

	def assertMode(self,next):
		if ((next == 0) and ((self.mode == 1))):
			_hx_local_0 = self
			_hx_local_1 = _hx_local_0.index
			_hx_local_0.index = (_hx_local_1 + 1)
			_hx_local_1
		self.mode = next

	def addTransition(self,s0,s1,c):
		resize = False
		if (s0 >= self.K):
			self.K = (s0 + 1)
			resize = True
		if (s1 >= self.K):
			self.K = (s1 + 1)
			resize = True
		if resize:
			self.cost.nonDestructiveResize(self.K,self.T,0)
			self.src.nonDestructiveResize(self.K,self.T,-1)
			self.path.nonDestructiveResize(1,self.T,-1)
		self.path_valid = False
		self.assertMode(1)
		if (self.index >= self.T):
			self.T = (self.index + 1)
			self.cost.nonDestructiveResize(self.K,self.T,0)
			self.src.nonDestructiveResize(self.K,self.T,-1)
			self.path.nonDestructiveResize(1,self.T,-1)
		sourced = False
		if (self.index > 0):
			c = (c + self.cost.get(s0,(self.index - 1)))
			sourced = (self.src.get(s0,(self.index - 1)) != -1)
		else:
			sourced = True
		if sourced:
			if ((c < self.cost.get(s1,self.index)) or ((self.src.get(s1,self.index) == -1))):
				self.cost.set(s1,self.index,c)
				self.src.set(s1,self.index,s0)

	def endTransitions(self):
		self.path_valid = False
		self.assertMode(0)

	def beginTransitions(self):
		self.path_valid = False
		self.assertMode(1)

	def calculatePath(self):
		if self.path_valid:
			return
		self.endTransitions()
		best = 0
		bestj = -1
		if (self.index <= 0):
			self.path_valid = True
			return
		_g1 = 0
		_g = self.K
		while (_g1 < _g):
			j = _g1
			_g1 = (_g1 + 1)
			if ((((self.cost.get(j,(self.index - 1)) < best) or ((bestj == -1)))) and ((self.src.get(j,(self.index - 1)) != -1))):
				best = self.cost.get(j,(self.index - 1))
				bestj = j
		self.best_cost = best
		_g11 = 0
		_g2 = self.index
		while (_g11 < _g2):
			j1 = _g11
			_g11 = (_g11 + 1)
			i = ((self.index - 1) - j1)
			self.path.set(0,i,bestj)
			if (not (((bestj != -1) and (((bestj >= 0) and ((bestj < self.K))))))):
				print(str("Problem in Viterbi"))
			bestj = self.src.get(bestj,i)
		self.path_valid = True

	def toString(self):
		self.calculatePath()
		txt = ""
		_g1 = 0
		_g = self.index
		while (_g1 < _g):
			i = _g1
			_g1 = (_g1 + 1)
			if (self.path.get(0,i) == -1):
				txt = (("null" if txt is None else txt) + "*")
			else:
				txt = (("null" if txt is None else txt) + Std.string(self.path.get(0,i)))
			if (self.K >= 10):
				txt = (("null" if txt is None else txt) + " ")
		txt = (("null" if txt is None else txt) + HxOverrides.stringOrNull(((" costs " + Std.string(self.getCost())))))
		return txt

	def length(self):
		if (self.index > 0):
			self.calculatePath()
		return self.index

	def get(self,i):
		self.calculatePath()
		return self.path.get(0,i)

	def getCost(self):
		self.calculatePath()
		return self.best_cost

Viterbi._hx_class = Viterbi


class haxe_IMap:
	_hx_class_name = "haxe.IMap"
	_hx_methods = ["get"]
haxe_IMap._hx_class = haxe_IMap


class haxe_ds_IntMap:
	_hx_class_name = "haxe.ds.IntMap"
	_hx_fields = ["h"]
	_hx_methods = ["set", "get", "remove", "keys", "toString"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		self.h = None
		self.h = dict()

	def set(self,key,value):
		self.h[key] = value

	def get(self,key):
		return self.h.get(key,None)

	def remove(self,key):
		if (not key in self.h):
			return False
		del self.h[key]
		return True

	def keys(self):
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def toString(self):
		s_b = python_lib_io_StringIO()
		s_b.write("{")
		it = self.keys()
		_hx_local_0 = it
		while _hx_local_0.hasNext():
			i = _hx_local_0.next()
			s_b.write(Std.string(i))
			s_b.write(" => ")
			x = Std.string(self.h.get(i,None))
			s_b.write(Std.string(x))
			if it.hasNext():
				s_b.write(", ")
		s_b.write("}")
		return s_b.getvalue()

haxe_ds_IntMap._hx_class = haxe_ds_IntMap


class haxe_ds_StringMap:
	_hx_class_name = "haxe.ds.StringMap"
	_hx_fields = ["h"]
	_hx_methods = ["get", "keys", "iterator"]
	_hx_interfaces = [haxe_IMap]

	def __init__(self):
		self.h = None
		self.h = dict()

	def get(self,key):
		return self.h.get(key,None)

	def keys(self):
		this1 = None
		_this = self.h.keys()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

	def iterator(self):
		this1 = None
		_this = self.h.values()
		this1 = iter(_this)
		return python_HaxeIterator(this1)

haxe_ds_StringMap._hx_class = haxe_ds_StringMap


class haxe_format_JsonPrinter:
	_hx_class_name = "haxe.format.JsonPrinter"
	_hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
	_hx_methods = ["write", "fieldsString", "quote"]
	_hx_statics = ["print"]

	def __init__(self,replacer,space):
		self.buf = None
		self.replacer = None
		self.indent = None
		self.pretty = None
		self.nind = None
		self.replacer = replacer
		self.indent = space
		self.pretty = (space is not None)
		self.nind = 0
		self.buf = StringBuf()

	def write(self,k,v):
		if (self.replacer is not None):
			v = self.replacer(k,v)
		_g = Type.typeof(v)
		if ((_g.index) == 8):
			self.buf.b.write("\"???\"")
		elif ((_g.index) == 4):
			self.fieldsString(v,python_Boot.fields(v))
		elif ((_g.index) == 1):
			v1 = v
			self.buf.b.write(Std.string(v1))
		elif ((_g.index) == 2):
			v2 = None
			def _hx_local_0():
				f = v
				return (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
			if _hx_local_0():
				v2 = v
			else:
				v2 = "null"
			self.buf.b.write(Std.string(v2))
		elif ((_g.index) == 5):
			self.buf.b.write("\"<fun>\"")
		elif ((_g.index) == 6):
			c = _g.params[0]
			if (c == str):
				self.quote(v)
			elif (c == list):
				v3 = v
				s = "".join(map(chr,[91]))
				self.buf.b.write(s)
				_hx_len = len(v3)
				last = (_hx_len - 1)
				_g1 = 0
				while (_g1 < _hx_len):
					i = _g1
					_g1 = (_g1 + 1)
					if (i > 0):
						s1 = "".join(map(chr,[44]))
						self.buf.b.write(s1)
					else:
						_hx_local_1 = self
						_hx_local_2 = _hx_local_1.nind
						_hx_local_1.nind = (_hx_local_2 + 1)
						_hx_local_2
					if self.pretty:
						s2 = "".join(map(chr,[10]))
						self.buf.b.write(s2)
					if self.pretty:
						v4 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
						self.buf.b.write(Std.string(v4))
					self.write(i,(v3[i] if i >= 0 and i < len(v3) else None))
					if (i == last):
						_hx_local_3 = self
						_hx_local_4 = _hx_local_3.nind
						_hx_local_3.nind = (_hx_local_4 - 1)
						_hx_local_4
						if self.pretty:
							s3 = "".join(map(chr,[10]))
							self.buf.b.write(s3)
						if self.pretty:
							v5 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
							self.buf.b.write(Std.string(v5))
				s4 = "".join(map(chr,[93]))
				self.buf.b.write(s4)
			elif (c == haxe_ds_StringMap):
				v6 = v
				o = _hx_AnonObject({})
				_hx_local_5 = v6.keys()
				while _hx_local_5.hasNext():
					k1 = _hx_local_5.next()
					value = v6.h.get(k1,None)
					setattr(o,(("_hx_" + k1) if (k1 in python_Boot.keywords) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
				self.fieldsString(o,python_Boot.fields(o))
			elif (c == Date):
				v7 = v
				self.quote(v7.toString())
			else:
				self.fieldsString(v,python_Boot.fields(v))
		elif ((_g.index) == 7):
			i1 = None
			e = v
			i1 = e.index
			v8 = i1
			self.buf.b.write(Std.string(v8))
		elif ((_g.index) == 3):
			v9 = v
			self.buf.b.write(Std.string(v9))
		elif ((_g.index) == 0):
			self.buf.b.write("null")
		else:
			pass

	def fieldsString(self,v,fields):
		s = "".join(map(chr,[123]))
		self.buf.b.write(s)
		_hx_len = len(fields)
		last = (_hx_len - 1)
		first = True
		_g = 0
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			f = (fields[i] if i >= 0 and i < len(fields) else None)
			value = Reflect.field(v,f)
			if Reflect.isFunction(value):
				continue
			if first:
				_hx_local_0 = self
				_hx_local_1 = _hx_local_0.nind
				_hx_local_0.nind = (_hx_local_1 + 1)
				_hx_local_1
				first = False
			else:
				s1 = "".join(map(chr,[44]))
				self.buf.b.write(s1)
			if self.pretty:
				s2 = "".join(map(chr,[10]))
				self.buf.b.write(s2)
			if self.pretty:
				v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
				self.buf.b.write(Std.string(v1))
			self.quote(f)
			s3 = "".join(map(chr,[58]))
			self.buf.b.write(s3)
			if self.pretty:
				s4 = "".join(map(chr,[32]))
				self.buf.b.write(s4)
			self.write(f,value)
			if (i == last):
				_hx_local_2 = self
				_hx_local_3 = _hx_local_2.nind
				_hx_local_2.nind = (_hx_local_3 - 1)
				_hx_local_3
				if self.pretty:
					s5 = "".join(map(chr,[10]))
					self.buf.b.write(s5)
				if self.pretty:
					v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
					self.buf.b.write(Std.string(v2))
		s6 = "".join(map(chr,[125]))
		self.buf.b.write(s6)

	def quote(self,s):
		s1 = "".join(map(chr,[34]))
		self.buf.b.write(s1)
		i = 0
		while True:
			c = None
			index = i
			i = (i + 1)
			if (index >= len(s)):
				c = -1
			else:
				c = ord(s[index])
			if (c == -1):
				break
			if (c == 34):
				self.buf.b.write("\\\"")
			elif (c == 92):
				self.buf.b.write("\\\\")
			elif (c == 10):
				self.buf.b.write("\\n")
			elif (c == 13):
				self.buf.b.write("\\r")
			elif (c == 9):
				self.buf.b.write("\\t")
			elif (c == 8):
				self.buf.b.write("\\b")
			elif (c == 12):
				self.buf.b.write("\\f")
			else:
				s2 = "".join(map(chr,[c]))
				self.buf.b.write(s2)
		s3 = "".join(map(chr,[34]))
		self.buf.b.write(s3)

	@staticmethod
	def print(o,replacer = None,space = None):
		printer = haxe_format_JsonPrinter(replacer, space)
		printer.write("",o)
		return printer.buf.b.getvalue()

haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter


class python_Boot:
	_hx_class_name = "python.Boot"
	_hx_statics = ["keywords", "toString1", "fields", "simpleField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "prefixLength", "unhandleKeywords"]

	@staticmethod
	def toString1(o,s):
		if (o is None):
			return "null"
		if isinstance(o,str):
			return o
		if (s is None):
			s = ""
		if (len(s) >= 5):
			return "<...>"
		if isinstance(o,bool):
			if o:
				return "true"
			else:
				return "false"
		if isinstance(o,int):
			return str(o)
		if isinstance(o,float):
			try:
				if (o == int(o)):
					def _hx_local_1():
						def _hx_local_0():
							v = o
							return Math.floor((v + 0.5))
						return str(_hx_local_0())
					return _hx_local_1()
				else:
					return str(o)
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				e = _hx_e1
				return str(o)
		if isinstance(o,list):
			o1 = o
			l = len(o1)
			st = "["
			s = (("null" if s is None else s) + "\t")
			_g = 0
			while (_g < l):
				i = _g
				_g = (_g + 1)
				prefix = ""
				if (i > 0):
					prefix = ","
				st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
			st = (("null" if st is None else st) + "]")
			return st
		try:
			if hasattr(o,"toString"):
				return o.toString()
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		if (python_lib_Inspect.isfunction(o) or python_lib_Inspect.ismethod(o)):
			return "<function>"
		if hasattr(o,"__class__"):
			if isinstance(o,_hx_AnonObject):
				toStr = None
				try:
					fields = python_Boot.fields(o)
					fieldsStr = None
					_g1 = []
					_g11 = 0
					while (_g11 < len(fields)):
						f = (fields[_g11] if _g11 >= 0 and _g11 < len(fields) else None)
						_g11 = (_g11 + 1)
						x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
						_g1.append(x)
					fieldsStr = _g1
					toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
				except Exception as _hx_e:
					_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
					e2 = _hx_e1
					return "{ ... }"
				if (toStr is None):
					return "{ ... }"
				else:
					return toStr
			if isinstance(o,Enum):
				o2 = o
				l1 = len(o2.params)
				hasParams = (l1 > 0)
				if hasParams:
					paramsStr = ""
					_g2 = 0
					while (_g2 < l1):
						i1 = _g2
						_g2 = (_g2 + 1)
						prefix1 = ""
						if (i1 > 0):
							prefix1 = ","
						paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix1 is None else prefix1) + HxOverrides.stringOrNull(python_Boot.toString1((o2.params[i1] if i1 >= 0 and i1 < len(o2.params) else None),s))))))
					return (((HxOverrides.stringOrNull(o2.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
				else:
					return o2.tag
			if hasattr(o,"_hx_class_name"):
				if (o.__class__.__name__ != "type"):
					fields1 = python_Boot.getInstanceFields(o)
					fieldsStr1 = None
					_g3 = []
					_g12 = 0
					while (_g12 < len(fields1)):
						f1 = (fields1[_g12] if _g12 >= 0 and _g12 < len(fields1) else None)
						_g12 = (_g12 + 1)
						x1 = ((("" + ("null" if f1 is None else f1)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f1),(("null" if s is None else s) + "\t"))))
						_g3.append(x1)
					fieldsStr1 = _g3
					toStr1 = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr1]))) + " )")
					return toStr1
				else:
					fields2 = python_Boot.getClassFields(o)
					fieldsStr2 = None
					_g4 = []
					_g13 = 0
					while (_g13 < len(fields2)):
						f2 = (fields2[_g13] if _g13 >= 0 and _g13 < len(fields2) else None)
						_g13 = (_g13 + 1)
						x2 = ((("" + ("null" if f2 is None else f2)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f2),(("null" if s is None else s) + "\t"))))
						_g4.append(x2)
					fieldsStr2 = _g4
					toStr2 = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr2]))) + " )")
					return toStr2
			if (o == str):
				return "#String"
			if (o == list):
				return "#Array"
			if callable(o):
				return "function"
			try:
				if hasattr(o,"__repr__"):
					return o.__repr__()
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				pass
			if hasattr(o,"__str__"):
				return o.__str__([])
			if hasattr(o,"__name__"):
				return o.__name__
			return "???"
		else:
			return str(o)

	@staticmethod
	def fields(o):
		a = []
		if (o is not None):
			if hasattr(o,"_hx_fields"):
				fields = o._hx_fields
				return list(fields)
			if isinstance(o,_hx_AnonObject):
				d = o.__dict__
				keys = d.keys()
				handler = python_Boot.unhandleKeywords
				for k in keys:
					a.append(handler(k))
			elif hasattr(o,"__dict__"):
				a1 = []
				d1 = o.__dict__
				keys1 = d1.keys()
				for k in keys1:
					a.append(k)
		return a

	@staticmethod
	def simpleField(o,field):
		if (field is None):
			return None
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def field(o,field):
		if (field is None):
			return None
		_hx_local_0 = len(field)
		if (_hx_local_0 == 6):
			if (field == "length"):
				if isinstance(o,str):
					s = o
					return len(s)
				elif isinstance(o,list):
					x = o
					return len(x)
			elif (field == "charAt"):
				if isinstance(o,str):
					s3 = o
					def _hx_local_1(a1):
						return HxString.charAt(s3,a1)
					return _hx_local_1
			elif (field == "substr"):
				if isinstance(o,str):
					s8 = o
					def _hx_local_2(a14):
						return HxString.substr(s8,a14)
					return _hx_local_2
			elif (field == "filter"):
				if isinstance(o,list):
					x5 = o
					def _hx_local_3(f1):
						return python_internal_ArrayImpl.filter(x5,f1)
					return _hx_local_3
			elif (field == "concat"):
				if isinstance(o,list):
					a16 = o
					def _hx_local_4(a21):
						return python_internal_ArrayImpl.concat(a16,a21)
					return _hx_local_4
			elif (field == "insert"):
				if isinstance(o,list):
					a3 = o
					def _hx_local_5(a17,x8):
						python_internal_ArrayImpl.insert(a3,a17,x8)
					return _hx_local_5
			elif (field == "remove"):
				if isinstance(o,list):
					x13 = o
					def _hx_local_6(e2):
						return python_internal_ArrayImpl.remove(x13,e2)
					return _hx_local_6
			elif (field == "splice"):
				if isinstance(o,list):
					x17 = o
					def _hx_local_7(a19,a22):
						return python_internal_ArrayImpl.splice(x17,a19,a22)
					return _hx_local_7
		elif (_hx_local_0 == 5):
			if (field == "split"):
				if isinstance(o,str):
					s7 = o
					def _hx_local_8(d):
						return HxString.split(s7,d)
					return _hx_local_8
			elif (field == "shift"):
				if isinstance(o,list):
					x14 = o
					def _hx_local_9():
						return python_internal_ArrayImpl.shift(x14)
					return _hx_local_9
			elif (field == "slice"):
				if isinstance(o,list):
					x15 = o
					def _hx_local_10(a18):
						return python_internal_ArrayImpl.slice(x15,a18)
					return _hx_local_10
		elif (_hx_local_0 == 11):
			if (field == "toLowerCase"):
				if isinstance(o,str):
					s1 = o
					def _hx_local_11():
						return HxString.toLowerCase(s1)
					return _hx_local_11
			elif (field == "toUpperCase"):
				if isinstance(o,str):
					s2 = o
					def _hx_local_12():
						return HxString.toUpperCase(s2)
					return _hx_local_12
			elif (field == "lastIndexOf"):
				if isinstance(o,str):
					s6 = o
					def _hx_local_13(a13):
						return HxString.lastIndexOf(s6,a13)
					return _hx_local_13
				elif isinstance(o,list):
					a2 = o
					def _hx_local_14(x2):
						return python_internal_ArrayImpl.lastIndexOf(a2,x2)
					return _hx_local_14
		elif (_hx_local_0 == 4):
			if (field == "copy"):
				if isinstance(o,list):
					def _hx_local_15():
						x6 = o
						return list(x6)
					return _hx_local_15
			elif (field == "join"):
				if isinstance(o,list):
					def _hx_local_16(sep):
						x9 = o
						return sep.join([python_Boot.toString1(x1,'') for x1 in x9])
					return _hx_local_16
			elif (field == "push"):
				if isinstance(o,list):
					x11 = o
					def _hx_local_17(e):
						return python_internal_ArrayImpl.push(x11,e)
					return _hx_local_17
			elif (field == "sort"):
				if isinstance(o,list):
					x16 = o
					def _hx_local_18(f2):
						python_internal_ArrayImpl.sort(x16,f2)
					return _hx_local_18
		elif (_hx_local_0 == 10):
			if (field == "charCodeAt"):
				if isinstance(o,str):
					s4 = o
					def _hx_local_19(a11):
						return HxString.charCodeAt(s4,a11)
					return _hx_local_19
		elif (_hx_local_0 == 3):
			if (field == "map"):
				if isinstance(o,list):
					x4 = o
					def _hx_local_20(f):
						return python_internal_ArrayImpl.map(x4,f)
					return _hx_local_20
			elif (field == "pop"):
				if isinstance(o,list):
					x10 = o
					def _hx_local_21():
						return python_internal_ArrayImpl.pop(x10)
					return _hx_local_21
		elif (_hx_local_0 == 9):
			if (field == "substring"):
				if isinstance(o,str):
					s9 = o
					def _hx_local_22(a15):
						return HxString.substring(s9,a15)
					return _hx_local_22
		elif (_hx_local_0 == 8):
			if (field == "toString"):
				if isinstance(o,str):
					s10 = o
					def _hx_local_23():
						return HxString.toString(s10)
					return _hx_local_23
				elif isinstance(o,list):
					x3 = o
					def _hx_local_24():
						return python_internal_ArrayImpl.toString(x3)
					return _hx_local_24
			elif (field == "iterator"):
				if isinstance(o,list):
					x7 = o
					def _hx_local_25():
						return python_internal_ArrayImpl.iterator(x7)
					return _hx_local_25
		elif (_hx_local_0 == 7):
			if (field == "indexOf"):
				if isinstance(o,str):
					s5 = o
					def _hx_local_26(a12):
						return HxString.indexOf(s5,a12)
					return _hx_local_26
				elif isinstance(o,list):
					a = o
					def _hx_local_27(x1):
						return python_internal_ArrayImpl.indexOf(a,x1)
					return _hx_local_27
			elif (field == "unshift"):
				if isinstance(o,list):
					x12 = o
					def _hx_local_28(e1):
						python_internal_ArrayImpl.unshift(x12,e1)
					return _hx_local_28
			elif (field == "reverse"):
				if isinstance(o,list):
					a4 = o
					def _hx_local_29():
						python_internal_ArrayImpl.reverse(a4)
					return _hx_local_29
		else:
			pass
		field1 = None
		if field in python_Boot.keywords:
			field1 = ("_hx_" + field)
		elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
			field1 = ("_hx_" + field)
		else:
			field1 = field
		if hasattr(o,field1):
			return getattr(o,field1)
		else:
			return None

	@staticmethod
	def getInstanceFields(c):
		f = None
		if hasattr(c,"_hx_fields"):
			f = c._hx_fields
		else:
			f = []
		if hasattr(c,"_hx_methods"):
			a = c._hx_methods
			f = (f + a)
		sc = python_Boot.getSuperClass(c)
		if (sc is None):
			return f
		else:
			scArr = python_Boot.getInstanceFields(sc)
			scMap = set(scArr)
			res = []
			_g = 0
			while (_g < len(f)):
				f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
				_g = (_g + 1)
				if (not f1 in scMap):
					scArr.append(f1)
			return scArr

	@staticmethod
	def getSuperClass(c):
		if (c is None):
			return None
		try:
			if hasattr(c,"_hx_super"):
				return c._hx_super
			return None
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			pass
		return None

	@staticmethod
	def getClassFields(c):
		if hasattr(c,"_hx_statics"):
			x = c._hx_statics
			return list(x)
		else:
			return []

	@staticmethod
	def unhandleKeywords(name):
		if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
			real = HxString.substr(name,python_Boot.prefixLength,None)
			if real in python_Boot.keywords:
				return real
		return name
python_Boot._hx_class = python_Boot


class python_HaxeIterator:
	_hx_class_name = "python.HaxeIterator"
	_hx_fields = ["it", "x", "has", "checked"]
	_hx_methods = ["next", "hasNext"]

	def __init__(self,it):
		self.it = None
		self.x = None
		self.has = None
		self.checked = None
		self.checked = False
		self.has = False
		self.x = None
		self.it = it

	def next(self):
		if (not self.checked):
			self.hasNext()
		self.checked = False
		return self.x

	def hasNext(self):
		if (not self.checked):
			try:
				self.x = self.it.__next__()
				self.has = True
			except Exception as _hx_e:
				_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
				if isinstance(_hx_e1, StopIteration):
					s = _hx_e1
					self.has = False
					self.x = None
				else:
					raise _hx_e
			self.checked = True
		return self.has

python_HaxeIterator._hx_class = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
	_hx_class_name = "python._KwArgs.KwArgs_Impl_"
	_hx_statics = ["fromT"]

	@staticmethod
	def fromT(d):
		d1 = python_Lib.anonAsDict(d)
		return d1
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_


class python_Lib:
	_hx_class_name = "python.Lib"
	_hx_statics = ["dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon"]

	@staticmethod
	def dictToAnon(v):
		return _hx_AnonObject(v.copy())

	@staticmethod
	def anonToDict(o):
		if isinstance(o,_hx_AnonObject):
			return o.__dict__.copy()
		else:
			return None

	@staticmethod
	def anonAsDict(o):
		if isinstance(o,_hx_AnonObject):
			return o.__dict__
		else:
			return None

	@staticmethod
	def dictAsAnon(d):
		return _hx_AnonObject(d)
python_Lib._hx_class = python_Lib


class python_internal_ArrayImpl:
	_hx_class_name = "python.internal.ArrayImpl"
	_hx_statics = ["concat", "iterator", "indexOf", "lastIndexOf", "toString", "pop", "push", "unshift", "remove", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set"]

	@staticmethod
	def concat(a1,a2):
		return (a1 + a2)

	@staticmethod
	def iterator(x):
		return python_HaxeIterator(x.__iter__())

	@staticmethod
	def indexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = 0
		elif (fromIndex < 0):
			l = (_hx_len + fromIndex)
		else:
			l = fromIndex
		if (l < 0):
			l = 0
		_g = l
		while (_g < _hx_len):
			i = _g
			_g = (_g + 1)
			if (a[i] == x):
				return i
		return -1

	@staticmethod
	def lastIndexOf(a,x,fromIndex = None):
		_hx_len = len(a)
		l = None
		if (fromIndex is None):
			l = _hx_len
		elif (fromIndex < 0):
			l = ((_hx_len + fromIndex) + 1)
		else:
			l = (fromIndex + 1)
		if (l > _hx_len):
			l = _hx_len
		def _hx_local_1():
			nonlocal l
			l = (l - 1)
			return l
		while (_hx_local_1() > -1):
			if (a[l] == x):
				return l
		return -1

	@staticmethod
	def toString(x):
		return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

	@staticmethod
	def pop(x):
		if (len(x) == 0):
			return None
		else:
			return x.pop()

	@staticmethod
	def push(x,e):
		x.append(e)
		return len(x)

	@staticmethod
	def unshift(x,e):
		x.insert(0, e)

	@staticmethod
	def remove(x,e):
		try:
			x.remove(e)
			return True
		except Exception as _hx_e:
			_hx_e1 = _hx_e.val if isinstance(_hx_e, _HxException) else _hx_e
			e1 = _hx_e1
			return False

	@staticmethod
	def shift(x):
		if (len(x) == 0):
			return None
		return x.pop(0)

	@staticmethod
	def slice(x,pos,end = None):
		return x[pos:end]

	@staticmethod
	def sort(x,f):
		x.sort(key= python_lib_Functools.cmp_to_key(f))

	@staticmethod
	def splice(x,pos,len):
		if (pos < 0):
			pos = (len(x) + pos)
		if (pos < 0):
			pos = 0
		res = x[pos:(pos + len)]
		del x[pos:(pos + len)]
		return res

	@staticmethod
	def map(x,f):
		return list(map(f,x))

	@staticmethod
	def filter(x,f):
		return list(filter(f,x))

	@staticmethod
	def insert(a,pos,x):
		a.insert(pos, x)

	@staticmethod
	def reverse(a):
		a.reverse()

	@staticmethod
	def _get(x,idx):
		if ((idx > -1) and ((idx < len(x)))):
			return x[idx]
		else:
			return None

	@staticmethod
	def _set(x,idx,v):
		l = len(x)
		while (l < idx):
			x.append(None)
			l = (l + 1)
		if (l == idx):
			x.append(v)
		else:
			x[idx] = v
		return v
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl


class _HxException(Exception):
	_hx_class_name = "_HxException"
	_hx_fields = ["val"]
	_hx_methods = []
	_hx_statics = []
	_hx_interfaces = []
	_hx_super = Exception


	def __init__(self,val):
		self.val = None
		message = str(val)
		super().__init__(message)
		self.val = val

_HxException._hx_class = _HxException


class HxOverrides:
	_hx_class_name = "HxOverrides"
	_hx_statics = ["iterator", "eq", "stringOrNull", "modf", "mapKwArgs"]

	@staticmethod
	def iterator(x):
		if isinstance(x,list):
			return python_HaxeIterator(x.__iter__())
		return x.iterator()

	@staticmethod
	def eq(a,b):
		if (isinstance(a,list) or isinstance(b,list)):
			return a is b
		return (a == b)

	@staticmethod
	def stringOrNull(s):
		if (s is None):
			return "null"
		else:
			return s

	@staticmethod
	def modf(a,b):
		return float('nan') if (b == 0.0) else a % b if a > 0 else -(-a % b)

	@staticmethod
	def mapKwArgs(a,v):
		a1 = python_Lib.dictAsAnon(python_Lib.anonToDict(a))
		def _hx_local_0():
			_this = v.keys()
			def _hx_local_2():
				def _hx_local_1():
					this1 = iter(_this)
					return python_HaxeIterator(this1)
				return _hx_local_1()
			return _hx_local_2()
		_hx_local_3 = _hx_local_0()
		while _hx_local_3.hasNext():
			k = _hx_local_3.next()
			val = v.get(k)
			if hasattr(a1,k):
				x = getattr(a1,k)
				setattr(a1,val,x)
				delattr(a1,k)
		return a1
HxOverrides._hx_class = HxOverrides


class HxString:
	_hx_class_name = "HxString"
	_hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "toString", "substring", "substr"]

	@staticmethod
	def split(s,d):
		if (d == ""):
			return list(s)
		else:
			return s.split(d)

	@staticmethod
	def charCodeAt(s,index):
		if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
			return None
		else:
			return ord(s[index])

	@staticmethod
	def charAt(s,index):
		if ((index < 0) or ((index >= len(s)))):
			return ""
		else:
			return s[index]

	@staticmethod
	def lastIndexOf(s,str,startIndex = None):
		if (startIndex is None):
			return s.rfind(str, 0, len(s))
		else:
			i = s.rfind(str, 0, (startIndex + 1))
			startLeft = None
			if (i == -1):
				startLeft = max(0,((startIndex + 1) - len(str)))
			else:
				startLeft = (i + 1)
			check = s.find(str, startLeft, len(s))
			if ((check > i) and ((check <= startIndex))):
				return check
			else:
				return i

	@staticmethod
	def toUpperCase(s):
		return s.upper()

	@staticmethod
	def toLowerCase(s):
		return s.lower()

	@staticmethod
	def indexOf(s,str,startIndex = None):
		if (startIndex is None):
			return s.find(str)
		else:
			return s.find(str, startIndex)

	@staticmethod
	def toString(s):
		return s

	@staticmethod
	def substring(s,startIndex,endIndex = None):
		if (startIndex < 0):
			startIndex = 0
		if (endIndex is None):
			return s[startIndex:]
		else:
			if (endIndex < 0):
				endIndex = 0
			if (endIndex < startIndex):
				return s[endIndex:startIndex]
			else:
				return s[startIndex:endIndex]

	@staticmethod
	def substr(s,startIndex,len = None):
		if (len is None):
			return s[startIndex:]
		else:
			if (len == 0):
				return ""
			return s[startIndex:(startIndex + len)]
HxString._hx_class = HxString

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

Coopy.VERSION = "1.2.6"
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")

Coopy.main()